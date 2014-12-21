from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty
from kivy.lang import Builder
import xmlrpclib
from kivy.storage.jsonstore import JsonStore
#store = JsonStore('hello.json')
Builder.load_string('''
#:import JsonStore kivy.storage.jsonstore
#:import random random.random
#:import SlideTransition kivy.uix.screenmanager.SlideTransition
#:import SwapTransition kivy.uix.screenmanager.SwapTransition
#:import WipeTransition kivy.uix.screenmanager.WipeTransition
#:import FadeTransition kivy.uix.screenmanager.FadeTransition
#:import RiseInTransition kivy.uix.screenmanager.RiseInTransition
#:import FallOutTransition kivy.uix.screenmanager.FallOutTransition
#:import NoTransition kivy.uix.screenmanager.NoTransition
<FirstBox>:
    
    
    BoxLayout:
        orientation:'vertical'
        BoxLayout:
            size_hint_y:None
            height:70
            Label:
                text:'Odoo App By Jamshi...'
        TextInput:
            id:ip
            border:[16,16,16,4]
            hint_text:'server ip'
            size_hint_y:None
            height:70
        TextInput:
            id:db
            hint_text:'database'
            size_hint_y:None
            height:70
        TextInput:
            id:port
            hint_text:'port'
            size_hint_y:None
            height:70
        TextInput:
            id:user
            hint_text:'username'
            size_hint_y:None
            height:70
        TextInput:
            id:passwd
            hint_text:'password'
            password:True
            size_hint_y:None
            height:70
        BoxLayout:
            orientation:'horizontal'
            Button:
                text:'login'
                background_color:[0,1,0,1]
                on_release:root.login()
            Button:
                text:'Quit'
                background_color:[0,0,1,1]
                on_release:App.on_stop()
        
        Label:
            id:status
            text:'Not Logged in...'
    
<MainMenu>:
    BoxLayout:
        orientation:'vertical'
        Button:
            text:'Create Customer'
            on_release:root.go_to_customer()
        Button:
            text:'Create Supplier'
            on_release:root.go_to_supplier()
        Button:
            text:'Creat Users'
            on_release:root.manager.current = 'user'
        Button:
            text:'Create Company'
            on_release:root.manager.current = 'company'
        Button:
            text:'Create Sale Order'
        Button:
            text:'Create Purchase Order'
        Button:
            text:'Quit'
            on_release:App.on_stop()
<Customer>:
    
    BoxLayout:
        orientation:'vertical'
        TextInput:
            id:name
            hint_text:'Customer Name'
            size_hint_y:None
            height:70
        TextInput:
            id:mobile
            hint_text:'Mobile'
            size_hint_y:None
            height:70
        TextInput:
            id:email
            hint_text:'email'
            size_hint_y:None
            height:70
            
        Button:
            text:'Create'
            on_release:root.create_customer()
        Button:
            text:'Main Menu'
            on_release:root.manager.current = 'main_menu'
        Button:
            text:'Quit'
            on_release:App.on_stop()
        
        Label:
            id:message
            text:'Enter Details to Add customer'
        Label:
            id:contact
            text:'Contact: +91 9744 894950'
        Label:
            text:'jamshu.mkd@gmail.com'
        Label:
            id:status
            text:'Not Created'

<Supplier>:
    
    BoxLayout:
        orientation:'vertical'
        TextInput:
            id:name
            hint_text:'Supplier Name'
            size_hint_y:None
            height:70
        TextInput:
            id:mobile
            hint_text:'Mobile'
            size_hint_y:None
            height:70
        TextInput:
            id:email
            hint_text:'email'
            size_hint_y:None
            height:70
            
        Button:
            text:'Create'
            on_release:root.create_supplier()
        Button:
            text:'Main Menu'
            on_release:root.manager.current = 'main_menu'
        Button:
            text:'Quit'
            on_release:App.on_stop()
        
        Label:
            id:message
            text:'Enter Details to Add customer'
        Label:
            id:contact
            text:'Contact: +91 9744 894950'
        Label:
            text:'jamshu.mkd@gmail.com'
        Label:
            id:status
            text:'Not Created'
<User>:
    
    BoxLayout:
        orientation:'vertical'
        TextInput:
            id:name
            hint_text:'User Name'
            size_hint_y:None
            height:70
        TextInput:
            id:login
            hint_text:'login'
            size_hint_y:None
            height:70
        TextInput:
            id:password
            hint_text:'password'
            size_hint_y:None
            height:70
        TextInput:
            id:email
            hint_text:'email'
            size_hint_y:None
            height:70
               
        Button:
            text:'Create'
            on_release:root.create_user()
        Button:
            text:'Main Menu'
            on_release:root.manager.current = 'main_menu'
        Button:
            text:'Quit'
            on_release:App.on_stop()
        
        Label:
            id:message
            text:'Enter Details to Add User'
       
        Label:
            id:status
            text:'Not Created'

<Company>:
    
    BoxLayout:
        orientation:'vertical'
        TextInput:
            id:name
            hint_text:'Company Name'
            size_hint_y:None
            height:70
       
               
        Button:
            text:'Create'
            on_release:root.create_company()
        Button:
            text:'Main Menu'
            on_release:root.manager.current = 'main_menu'
        Button:
            text:'Quit'
            on_release:App.on_stop()
        
        Label:
            id:message
            text:'Enter Details to Add Company'
       
        Label:
            id:status
            text:'Not Created'
''')

val = {}
class Customer(Screen):
       
    def create_customer(self,*agrs):
        if val.get('ip'):
            
            ip=val.get('ip')
            db=val.get('db')
            port =val.get('port')
            user=val.get('user')
            passwd=val.get('passwd')
            sock_common = xmlrpclib.ServerProxy ('http://'+ip+':'+port+'/xmlrpc/common', allow_none=True)
            uid = sock_common.login(db, user, passwd)
            sock= xmlrpclib.ServerProxy('http://'+ip+':'+port+'/xmlrpc/object', allow_none=True)
            customer_name =self.ids.name.text
            mobile = self.ids.mobile.text
            email=self.ids.email.text
            c_vals ={'name':customer_name,
                    'mobile':mobile,
                    'email':email,  
                    'customer':True}
            if customer_name != '':
                sock.execute(db, uid, passwd, 'res.partner', 'create', c_vals)
                self.ids.status.text = 'Customer Created Successfuly'
        
class Supplier(Screen):
    def create_supplier(self,*args):
        if val.get('ip'):
            
            ip=val.get('ip')
            db=val.get('db')
            port =val.get('port')
            user=val.get('user')
            passwd=val.get('passwd')
            sock_common = xmlrpclib.ServerProxy ('http://'+ip+':'+port+'/xmlrpc/common', allow_none=True)
            uid = sock_common.login(db, user, passwd)
            sock= xmlrpclib.ServerProxy('http://'+ip+':'+port+'/xmlrpc/object', allow_none=True)
            customer_name =self.ids.name.text
            mobile = self.ids.mobile.text
            email=self.ids.email.text
            c_vals ={'name':customer_name,
                    'mobile':mobile,
                    'email':email,
                    'supplier':True }
            if customer_name != '':
                sock.execute(db, uid, passwd, 'res.partner', 'create', c_vals)
                self.ids.status.text = 'Supplier Created Successfuly'

class User(Screen):
    def create_user(self,*args):
        if val.get('ip'):
            
            ip=val.get('ip')
            db=val.get('db')
            port =val.get('port')
            user=val.get('user')
            passwd=val.get('passwd')
            sock_common = xmlrpclib.ServerProxy ('http://'+ip+':'+port+'/xmlrpc/common', allow_none=True)
            uid = sock_common.login(db, user, passwd)
            sock= xmlrpclib.ServerProxy('http://'+ip+':'+port+'/xmlrpc/object', allow_none=True)
            name =self.ids.name.text
            login = self.ids.login.text
            email=self.ids.email.text
            password=self.ids.password.text
            c_vals ={'name':name,
                    'login':login,
                    'email':email,
                    'password':password}
            if name != '':
                sock.execute(db, uid, passwd, 'res.users', 'create', c_vals)
                self.ids.status.text = 'User Created Successfuly'

class Company(Screen):
    def create_company(self,*args):
        if val.get('ip'):
                
                ip=val.get('ip')
                db=val.get('db')
                port =val.get('port')
                user=val.get('user')
                passwd=val.get('passwd')
                sock_common = xmlrpclib.ServerProxy ('http://'+ip+':'+port+'/xmlrpc/common', allow_none=True)
                uid = sock_common.login(db, user, passwd)
                sock= xmlrpclib.ServerProxy('http://'+ip+':'+port+'/xmlrpc/object', allow_none=True)
                name =self.ids.name.text
                
                c_vals ={'name':name}
                if name != '':
                    sock.execute(db, uid, passwd, 'res.company', 'create', c_vals)
                    self.ids.status.text = 'Company Created Successfuly'
        
class FirstBox(Screen):
            
    def login(self,*args):
        ip = self.ids.ip.text
        db = self.ids.db.text
        port = self.ids.port.text
        user = self.ids.user.text
        passwd = self.ids.passwd.text
        global val 
        val ={'ip':ip,'db':db,'port':port,'user':user,'passwd':passwd}
        
        
        try:
            
            
            sock_common = xmlrpclib.ServerProxy ('http://'+ip+':'+port+'/xmlrpc/common', allow_none=True)
            uid = sock_common.login(db, user, passwd)
            #store.put('tito', ip=ip, db=db,port=port,user=user,passwd=passwd)
            self.manager.current = 'main_menu'
        except Exception, e:
             self.ids.status.text='Login Failed Please Try Again'
        
class MainMenu(Screen):
    def go_to_customer(self,*args):
        self.manager.current = 'customer' 
    def go_to_supplier(self,*args):
        self.manager.current = 'supplier'   

class ScreenManagerApp(App):

    def build(self):
        self.title = 'OdooApp'
        root = ScreenManager()

        root.add_widget(FirstBox(name='first'))
        root.add_widget(MainMenu(name='main_menu'))
        root.add_widget(Customer(name='customer'))
        root.add_widget(Supplier(name='supplier'))
        root.add_widget(User(name='user'))
        root.add_widget(Company(name='company'))
        return root

if __name__ == '__main__':
    ScreenManagerApp().run()
