import { StatusBar } from 'react-native';
import Login from './Components/login';
import SignUp from './Components/SignUp';
import Register from './Components/Register';
import CustomerStore from './Components/CustomerStore';
import CustomerNavbar from './Components/CustomerNavbar';
import Cart from './Components/Cart';
import Details from './Components/Details';
import  Orders from './Components/Orders';
import Contribution from './Components/Contribution';
import Account from './Components/Account';
import CustomerPayment from './Components/CustomerPayment';
import ForgetPassword from './Components/ForgetPassword';
import OTP from './Components/OTP';
import CustomerProduct from './Components/CustomerProduct';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import { Header } from 'react-native-elements';

const Stack = createNativeStackNavigator();
export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName='CustomerStore'>
        <Stack.Screen name="Login" component={Login} options={{headerShown:false}}/>
        <Stack.Screen name="SignUp" component={SignUp} options={{headerShown:false}}/>
        <Stack.Screen name='Register' component={Register} options={{headerShown:false}}/>
        <Stack.Screen name='CustomerStore' component={CustomerStore} options={{headerShown:false}}/>
        <Stack.Screen name='Cart' component={Cart} options={{headerShown:false}}/>
        <Stack.Screen name='Account' component={Account} options={{headerShown:false}}/>
        <Stack.Screen name='Details' component={Details} options={{headerShown:false}}/>
        <Stack.Screen name='Orders' component={Orders} options={{headerShown:false}}/>
        <Stack.Screen name='Contribution' component={Contribution} options={{headerShown:false}}/>
        <Stack.Screen name='CustomerPayment' component={CustomerPayment} options={{headerShown:false}}/>

      </Stack.Navigator>
   </NavigationContainer>
    
    
  );
}