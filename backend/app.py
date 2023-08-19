from flask import Flask,jsonify,request
import mysql.connector
#from flask_mysqldb import MySQL
import os
import mysql.connector

app=Flask(__name__)
import mysql.connector

mydb = mysql.connector.connect(
  host="192.168.0.156",
  user="root",
  password="tiger",
  database="wtv"
)
'''
from flask import Flask, request, jsonify
import mysql.connector 
mydb=mysql.connector.connect(
    host= "172.31.99.34",
    user= "Madumitha",
    password= "1234",
    database="WASTETOVALUE"
)'''
app = Flask(__name__)
mycursor = mydb.cursor()
cur=mydb.cursor()
@app.route('/user',methods=['GET'])
def user():
    cur.execute("select * from login")
    result = cur.fetchall()
    return jsonify(result)
@app.route('/createuseraccount',methods=["POST"])
def createuseraccount():
    email=request.json['email']
    password=request.json['password']
    cur.execute("select email from login")
    result = cur.fetchall()
    exist=False
    for i in result :
        if i[0]== email:
            exist=True            
            break
    if exist==False:
        sql="insert into  login (password,type,email)values (%s,%s,%s)"
        val=(password,'user',email)
        cur.execute(sql,val)
        mydb.commit()
        return jsonify("Sucess")
    else:
        return jsonify("Account already exists")
    
@app.route('/customer',methods=["POST"])
def add():
    return jsonify("hai")


@app.route('/')

#for user details
@app.route('/userdetails/<int:id>',methods=["POST","GET"])
def userdetails(id):
    qury="select username from login where id="+id
    cur.execute(qury)
    result=cur.fetchall()
    print(id)
    if result[0][0]==None:
        username=request.json['username']
        sql="update login set username=%s where id="+id
        val=(username,)
        cur.execute(sql,val)
        mydb.commit()

        return jsonify("Updated the details")
    else:
        return jsonify("details allredy exist")

#for login
@app.route('/login', methods=['POST'])
def login():
    #data = request.get_json()
    email = request.json['email']
    password = request.json['password']
    sql = "SELECT * FROM login WHERE email = %s AND password = %s"
    val = (email, password)
    cur.execute(sql, val)
    user = cur.fetchone()
    
    if user:
        sql = "SELECT id FROM login WHERE email = %s"
        val = (email,)
        cur.execute(sql, val)
        userid = cur.fetchone()
        userid=userid[0]
        return jsonify({"message":"Login Successful","customer_id":userid})
    else:
        return jsonify("Incorrect email or password"), 401
    
# for signup

@app.route('/checkdetails/<int:customer_id>',methods=['GET','POST'])
def checkdetails(customer_id):
    check_name='select username from login where id=%s'
    cur.execute(check_name, [customer_id,]) 
    username = cur.fetchone()
    print(customer_id)
    print(username)
    if  username[0]!=None:
        return jsonify({"message":"Payment","customer_id":customer_id})
    else:
        return jsonify({"message":"Details","customer_id":customer_id})
@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    check_email_sql = "SELECT * FROM login WHERE email = %s"
    cur.execute(check_email_sql, [email])  

    user = cur.fetchone()

    if user:
        return jsonify("Email already exists")
    else:
        sql = "INSERT INTO login (type, email, password) VALUES (%s, %s, %s)"
        val = ['user', email, password]  
        cur.execute(sql, val)
        mydb.commit()

        return jsonify("Signup Successful")


#UPLOAD_FOLDER = 'uploads'
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/company', methods=['POST'])
def company():
    data = request.get_json()
    name=data.get('Companyname')
    email = data.get('email')
    ph_no=data.get('ph_no')
    address=data.get('address')
    pin=data.get('pin')
    password=data.get('password')
    query1="select * from login where email=%s"
    cur.execute(query1,(email,))
    user=cur.fetchone()
    if not user:
        return jsonify({"message":"Register as user"})
    else:
        if user[3]=='pending' or user[3]=='company':
            return jsonify({"message":"Already register"})
        if user[2]!=password:
            return jsonify({"message":"Incorrect password"})
        else:
            query="update login set company_name=%s, phonenumber=%s, address=%s, pincode=%s where email=%s"
            cur.execute(query,(name,ph_no,address,pin,email))
            mydb.commit()
            return jsonify("Registered successfully")

    


'''
@app.route('/api/products', methods=['GET'])
def get_productslist():
    try:
        connection = mysql.connector.connect(db_config)
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT id, pname FROM products") 
        products = cursor.fetchall()
        cursor.close()
        return jsonify(products)
    except Exception as e:
        return jsonify({'error': str(e)})


'''

products = []
@app.route('/api/add_product', methods=['POST'])
def add_product():
    try:
        data = request.get_json()
        product_name = data.get('product_name')
        product_description = data.get('product_description')
        product_price = data.get('product_price')
        products.append(data)
        cursor = mydb.cursor()
        query = "INSERT INTO productdetails (product_name, product_description, product_price) VALUES (%s, %s, %s)"
        values = (product_name, product_description, product_price)
        cursor.execute(query, values)
        mydb.commit()
        cursor.close()
        return jsonify({'message': 'Product added to database successfully'})
    except Exception as e:
        mydb.rollback()
        if 'cursor' in locals():
            cursor.close()
        return jsonify({'error': str(e)})

@app.route('/api/productslist', methods=['GET'])
def get_productslist():
    try:
        cursor = mydb.cursor(dictionary=True)
        query = "SELECT * FROM productdetails"
        cursor.execute(query)
        products = cursor.fetchall()
        cursor.close()
        print(products)
        return jsonify(products)
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/api/selectedproduct/<int:product_id>', methods=['GET'])
def get_product_details(product_id):
    cursor = mydb.cursor(dictionary=True)
    query = "SELECT * FROM productdetails WHERE product_id = %s"
    cursor.execute(query, (product_id,))
    product_details = cursor.fetchone()
    return jsonify(product_details)

@app.route('/api/add_to_cart', methods=['POST'])
def add_to_cart():
    try:
        data = request.get_json()
        customer_id = data.get('customer_id')
        product_id = data.get('product_id')

        cursor = mydb.cursor()
        query = "INSERT INTO addtocart (customer_id, product_id) VALUES (%s, %s)"
        values = (customer_id, product_id)

        cursor.execute(query, values)
        mydb.commit()
        cursor.close()

        return jsonify({'message': 'Product added to cart successfully'})
    except Exception as e:
        mydb.rollback()
        cursor.close()
        return jsonify({'error': 'Product already in cart'})
    
@app.route('/api/cartdetails/<int:customer_id>', methods=['GET'])
def cartdetails(customer_id):
    cursor=mydb.cursor(dictionary=True)
    query="Select * from addtocart left join productdetails on addtocart.product_id=productdetails.product_id where customer_id= %s"
    value=(customer_id,)
    cursor.execute(query,value)
    cartdata=cursor.fetchall()
    print('cartdata fetching:',cartdata)
    return jsonify(cartdata)


    # storing image data
    '''if image:
        filename = os.path.join('uploads', image.filename)
        image.save(filename)
        insert_sql = "INSERT INTO login (image) VALUES (%s)"
        image_data = image.read()  # Read binary image data
        val = [image_data]
        cur.execute(insert_sql, val)
        mydb.commit()
    '''
    
    return jsonify("You will be verified soon!!")
    


if __name__=="__main__":
    app.run(host='192.168.56.1',port='3000',debug=True)


'''

from flask import Flask, request, jsonify
import mysql.connector 
db=mysql.connector.connect(
    host= "localhost",
    user= "Madumitha",
    password= "madumitha",
    database="WASTETOVALUE"
)
app = Flask(__name__)


@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify(products)



if __name__ == '__main__':
    app.run(host='192.168.56.1',port='3000',debug=True)'''