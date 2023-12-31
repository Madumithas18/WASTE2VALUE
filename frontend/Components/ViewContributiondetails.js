import { View, Text,TouchableOpacity, TextInput,TouchableWithoutFeedback,Keyboard,FlatList } from 'react-native'
import React, { useEffect, useState } from 'react';
import {useFocusEffect} from "@react-navigation/native";
import { Alert } from 'react-native';
import { Header } from 'react-native-elements';
import { ScrollView } from 'react-native';
import Url from './Url';
const ViewContributionDetails=({navigation,route})=>{

    const {contribution_id,company_id} = route.params;
    const [Data,setData] = useState({});
    console.log(contribution_id,company_id);
   useEffect(()=>{
    getcontributiondetails()
   },[]);

   const handleYes=()=>{
          acceptContribution();
          navigation.navigate("Contribution",{company_id});
   }
   const acceptContribution=()=>{
    fetch(`${Url()}/api/acceptcontribution/`,{
        method:'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            company_id:company_id,
            contribution_id:contribution_id
        })
    })
    .then((response)=>response.json())
    .then((data)=>console.log(data))
    .catch((error)=>console.log(error))
   }

    const getcontributiondetails=()=>{
        fetch(`${Url()}/api/getcontributiondetails/${contribution_id}`)
        .then((response)=>response.json())
        .then((data)=>{
            console.log(data);
            setData(data)
        })
        .catch((error)=>{
            console.error(error);
        })
    }

    return(
        <ScrollView>

        <View style={{margin:10,marginBottom:60}}>

            <View style={{alignItems:'center',justifyContent:'center'}}><Text style={{fontSize:35, fontWeight:600}}>Contribution Details</Text></View>
            <View style={{alignItems:'left',margin:10}}>
            <View style={{top:20,padding:20,justifyContent:'center',borderWidth:2,borderColor:'black',borderRadius:12,height:180}}>
            <Text style={{fontSize:20, fontWeight:400, paddingTop:5}}>Contribution ID          : {contribution_id}</Text>
            <Text style={{fontSize:20, fontWeight:400, paddingTop:20}}>Customer ID                 : {Data[1]}</Text>
            <Text style={{fontSize:20, fontWeight:400, paddingTop:20}}>Customer userName  : {Data[2]}</Text>
            </View>
            <View style={{padding:20,flex:1,top:30,borderColor:'black',borderRadius:12,borderWidth:1}}>
            <Text style={{fontSize:23, fontWeight:300, paddingTop:20}}>Address :</Text>
            <View style={{marginLeft:70}}><Text style={{fontSize:23, fontWeight:600, paddingTop:10}}>{Data[3]}</Text></View>
            <Text style={{fontSize:23, fontWeight:300, paddingTop:20}}>District :</Text>
            <View style={{marginLeft:70}}><Text style={{fontSize:23, fontWeight:600, paddingTop:10}}>{Data[4]}</Text></View>
            <Text style={{fontSize:23, fontWeight:300, paddingTop:20}}>landmark :</Text>
            <View style={{marginLeft:70}}><Text style={{fontSize:23, fontWeight:600, paddingTop:10}}>{Data[5]}</Text></View>
            <Text style={{fontSize:23, fontWeight:300, paddingTop:20}}>pincode : </Text>
            <View style={{marginLeft:70}}><Text style={{fontSize:23, fontWeight:600, paddingTop:10}}>{Data[6]}</Text></View>

            </View>
            </View>
            
            <TouchableOpacity style={{top:40,justifyContent:'center',alignItems:'center'}} onPress={()=>Alert.alert("Accept contribution?","",[{text:"Yes", onPress:()=>handleYes()},{text:"No"}])}>
                <View style={{alignItems:'center',justifyContent:'center',height:70,width:280,backgroundColor:'pink',borderColor:'deeppink',borderWidth:1,elevation:12,borderRadius:12,shadowColor:'deeppink'}}>
                    <Text style={{fontSize:25}}>Accept Contribution</Text>
                </View>
            </TouchableOpacity>
        </View>
        </ScrollView>

    )

}

export default ViewContributionDetails;