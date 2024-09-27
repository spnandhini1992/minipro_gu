import pandas as pd
import pymysql
import streamlit as st 
from streamlit_option_menu import option_menu  #used for selecting an option from list of options in a menu
import plotly.express as px 
from tabulate import tabulate
import altair as alt

#each bus we have to filter
#now we have to take route_name from each dataframe and then append to list

#kerala bus
kerala=[]
df_k=pd.read_csv("C:/Users/umasu/Downloads/Nandhini/miniproject - redbus/df_k.csv")
for i,r in df_k.iterrows():  #each row traversing
    kerala.append(r['Route_name'])   # add that row in new list


#Andhra bus
andhra=[]
df_a=pd.read_csv("C:/Users/umasu/Downloads/Nandhini/miniproject - redbus/df_A.csv")
for i,r in df_a.iterrows():
    andhra.append(r['Route_name'])

#Assam bus
assam=[]
df_as=pd.read_csv("C:/Users/umasu/Downloads/Nandhini/miniproject - redbus/df_AS.csv")
for i,r in df_as.iterrows():
    assam.append(r['Route_name'])


#goa bus
goa=[]
df_g=pd.read_csv("C:/Users/umasu/Downloads/Nandhini/miniproject - redbus/df_G.csv")
for i,r in df_g.iterrows():
    goa.append(r['Route_name'])
    
#telangana
telangana=[]
df_t=pd.read_csv("C:/Users/umasu/Downloads/Nandhini/miniproject - redbus/df_T.csv")
for i,r in df_t.iterrows():
    telangana.append(r['Route_name'])

#haryana
haryana=[]
df_h=pd.read_csv("C:/Users/umasu/Downloads/Nandhini/miniproject - redbus/df_H.csv")
for i,r in df_h.iterrows():
    haryana.append(r['Route_name'])

#punjab bus
punjab=[]
df_pb=pd.read_csv("C:/Users/umasu/Downloads/Nandhini/miniproject - redbus/df_P.csv")
for i,r in df_pb.iterrows():
    punjab.append(r["Route_name"])

#rajasthan bus
rajasthan=[]
df_r=pd.read_csv("C:/Users/umasu/Downloads/Nandhini/miniproject - redbus/df_R.csv")
for i,r in df_r.iterrows():
    rajasthan.append(r['Route_name'])
    
#south bengal bus
sbengal=[]
df_s=pd.read_csv("C:/Users/umasu/Downloads/Nandhini/miniproject - redbus/df_SB.csv")
for i,r in df_s.iterrows():
    sbengal.append(r["Route_name"])
    
#uttar pradesh bus
up=[]
df_u=pd.read_csv("C:/Users/umasu/Downloads/Nandhini/miniproject - redbus/df_UP.csv")
for i,r in df_u.iterrows():
    up.append(r['Route_name'])

#west bengal bus
wbengal=[]
df_wb=pd.read_csv("C:/Users/umasu/Downloads/Nandhini/miniproject - redbus/df_WB.csv")
for i,r in df_wb.iterrows():
    wbengal.append(r['Route_name'])

#chandigarh bus
chandi=[]
df_c=pd.read_csv("C:/Users/umasu/Downloads/Nandhini/miniproject - redbus/df_C.csv")
for i,r in df_c.iterrows():
    chandi.append(r['Route_name'])


###############################################

# ---------------> STREAMLIT PART ------------>

###############################################



#setting streamlit page
st.set_page_config(layout="wide",page_icon=":material/directions_bus:",page_title="MiniPro Project",initial_sidebar_state="expanded")
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("https://www.shutterstock.com/image-vector/3d-realistic-bus-render-illustration-260nw-2401805639.jpg");
        background-size: cover; /* Ensures the image covers the entire container */
        background-position: center; /* Centers the image */
        background-repeat: no-repeat; /* Prevents the image from repeating */
        background-attachment: fixed; /* Fixes the image in place when scrolling */
        height: 100vh; /* Sets the height to 100% of the viewport height */
        width: 100vw; /* Sets the width to 100% of the viewport width */
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <style>
    [data-testid="stSidebar"] {{
        background-color: #60191900; /* Replace with your desired color */
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    /* Ensure font size does not change on hover */
    .nav-link {
        font-size: 18px !important;
    }
    .nav-link:hover {
        font-size: 18px !important;
        color: #32789e !important; /* Change only the color on hover */
    }
    .nav-link-selected {
        font-size: 20px !important;
    }
    </style>
    """,unsafe_allow_html=True
)




# Theme button in the sidebar



with st.sidebar:
    #THEME CONTROL  OPERATIONAL IN SIDEBAR
    
    
    menu = option_menu(
        "Main Menu", 
        ["Home", 'Bus Routes'], 
        icons=['house', 'map'], 
        menu_icon="cast", 
        default_index=0,
        styles={
            "icon":{"font-size":"21px"},
            # "nav-link-selected": {"background-color": "#0b0bdd","font-size":"20px"}
        }
    )


if menu=="Home":
    st.title(":orange[:material/analytics:] :blue[Data Scraping with Selenium  & Filtering using Streamlit]")
    st.text("") 
    st.subheader(" ")
    st.markdown(""" ### :blue[:material/tooltip:] :green[*Objective of the Project*]

                To Scrape the Data from Redbus Website and to create a user interface and 
     filtration of data using streamlit and SQL 
    """)
    
    dfbus=pd.read_csv("C:/Users/umasu/Downloads/Nandhini/miniproject - redbus/mod_redbus_data2.csv")
    
    st.markdown(" ### :blue[:material/box:] :green[*Analysis between Price and Ratings*]")

    fig = px.scatter(dfbus, 
                 x='Price', 
                 y='Ratings', 
                 color='Bus_type',
                 size='Seats_Available',
                 hover_name='Bus_name',
                 title='Bus Price vs Ratings',
                 labels={'Price': 'Ticket Price', 'Ratings': 'Bus Ratings'})

    # Display the plot in Streamlit
    st.plotly_chart(fig)
    
    st.markdown("""
                <br><br>""",unsafe_allow_html=True)
    
    labels = dfbus['Seats_Available']
    values = dfbus['Ratings']

     
    
    dfbus = pd.read_csv("C:/Users/umasu/Downloads/Nandhini/miniproject - redbus/mod_redbus_data2.csv")
   
if menu=="Bus Routes":
    
    st.title(":red[:material/filter_alt:]    :green[Filtering of Data]")
    
    
    col1,col2=st.columns(2)
    with col1:
        state=st.selectbox("List of States",["Kerala", "Andhra Pradesh", "Telangana", "Goa", "Rajasthan", "Punjab",
                                          "South Bengal", "Haryana", "Assam", "Uttar Pradesh", "West Bengal", "Chandigarh"])
    with col2:
        select_type=st.selectbox("choose bus type",["A/C","NON A/C","sleeper","semi-sleeper","seater","others"])
    with col1:
        fare = st.number_input("Enter fare", min_value=100, max_value=8000, value=100, step=50)
        #select_fare = st.number_input("Enter bus fare", min_value=40, max_value=5000, value=40, step=1)
    with col2:
        select_rating = st.slider("Choose rating", min_value=0, max_value=5, value=5, step=1)
    with col1:
        TIME=st.time_input("select the time")  
    #time_str=TIME.strftime("%H:%M:%S")  
    
    #KERALA BUS FILTERATION
    if state=="Kerala":
        with col2:
            k=st.selectbox("List of routes",kerala)
        
        #CREATE A FUNCTION FOR CONNNECTION TO SQL FILTERATION
        
        def type_and_fare(bus_type, fare_range,rate_range):
            conn=pymysql.connect(host="127.0.0.1",user="root",password="Chennai28&",database="vazhai",port=3306)
            my_cursor=conn.cursor()
            
            #filtration for rating
            rate_min, rate_max = 0, 5  # Default range
            if rate_range == 5:
                rate_min, rate_max = 4.1, 5.0
            elif rate_range == 4:
                rate_min, rate_max = 3.1, 4.0
            elif rate_range == 3:
                rate_min, rate_max = 2.1, 3.0
            elif rate_range == 2:
                rate_min, rate_max = 1.1, 2.0
            elif rate_range == 1:
                rate_min, rate_max = 0, 1.0
                #filteration for fare,bustype and rating
            
            
            #define bus type condition
            if bus_type=="sleeper":
                bus_type_option = "bustype LIKE '%Sleeper%'"
            elif bus_type=="semi-sleeper":
                bus_type_option = "bustype LIKE '%Semi Sleeper %'"
            elif bus_type=="A/C":
                bus_type_option = "bustype LIKE '% A/C %'"
            elif bus_type=="NON A/C":
                bus_type_option = "bustype LIKE '% NON A/C% '"
            elif bus_type=="seater":
                bus_type_option = "bustype LIKE '% Seater %'"
            else:
                bus_type_option = "bustype NOT LIKE '%Sleeper' AND bustype NOT LIKE '%Semi-Sleeper %' AND bustype NOT LIKE '% Seater %' AND bustype NOT LIKE '% A/C%' AND bustype NOT LIKE '%NON A/C %'"
            
            sqlquery= f""" 
                SELECT * FROM busdetail
                WHERE price <= {fare}
                AND route_name = '{k}' 
                AND {bus_type_option} AND start_time >= '{TIME}'
                AND star_rating BETWEEN {rate_min} and {rate_max}
                ORDER BY price and start_time DESC
            """
            
            my_cursor.execute(sqlquery)
            out=my_cursor.fetchall()
            conn.close()
            
            df=pd.DataFrame(out,columns=[
                "ID","Bus_name","Bus_type","Start_time","End_time","Duration","Price","Seats_Available","Ratings","Route_link","Route_name"
            ])
            
            return df
        df_result = type_and_fare(select_type,fare,select_rating)
        st.subheader("""
                    :blue[:material/refresh:] :blue[Result]
                    """)
        st.dataframe(df_result,use_container_width=True)
    
    
    #ANDHRA
    if state=="Andhra Pradesh":
        with col2:
            k=st.selectbox("List of routes",andhra)
        
        #CREATE A FUNCTION FOR CONNNECTION TO SQL FILTERATION
        
        def type_and_fare(bus_type, fare_range,rate_range):
            conn=pymysql.connect(host="127.0.0.1",user="root",password="Chennai28&",database="vazhai",port=3306)
            my_cursor=conn.cursor()
            
            #filtration for rating
            rate_min, rate_max = 0, 5  # Default range
            if rate_range == 5:
                rate_min, rate_max = 4.1, 5
            elif rate_range == 4:
                rate_min, rate_max = 3.1, 4.0
            elif rate_range == 3:
                rate_min, rate_max = 2.1, 3.0
            elif rate_range == 2: 
                rate_min, rate_max = 1.1, 2.0
            elif rate_range == 1:
                rate_min, rate_max = 0, 1.0
                #filteration for fare,bustype and rating
            
            
            #define bus type condition
            if bus_type=="sleeper":
                bus_type_option = "bustype LIKE '%Sleeper%'"
            elif bus_type=="semi-sleeper":
                bus_type_option = "bustype LIKE '%Semi Sleeper %'"
            elif bus_type=="A/C":
                bus_type_option = "bustype LIKE '% A/C %'"
            elif bus_type=="NON A/C":
                bus_type_option = "bustype LIKE '% NON A/C% '"
            elif bus_type=="seater":
                bus_type_option = "bustype LIKE '% Seater %'"
            else:
                bus_type_option = "bustype NOT LIKE '%Sleeper' AND bustype NOT LIKE '%Semi-Sleeper %' AND bustype NOT LIKE '% Seater %' AND bustype NOT LIKE '% A/C%' AND bustype NOT LIKE '%NON A/C %'"
            
            sqlquery= f""" 
                SELECT * FROM busdetail
                WHERE price <= {fare}
                AND route_name = '{k}' 
                AND {bus_type_option} AND start_time >= '{TIME}'
                AND star_rating BETWEEN {rate_min} and {rate_max}
                ORDER BY price and start_time DESC
            """
            
            my_cursor.execute(sqlquery)
            out=my_cursor.fetchall()
            conn.close()
            
            df=pd.DataFrame(out,columns=[
                "ID","Bus_name","Bus_type","Start_time","End_time","Duration","Price","Seats_Available","Ratings","Route_link","Route_name"
            ])
            
            return df
        df_result2 = type_and_fare(select_type,fare,select_rating)
        st.subheader("""
                    :blue[:material/resume:] :green[Result]
                    """)
        st.dataframe(df_result2,use_container_width=True)
        
    #PUNJAB 
    
    if state=="Punjab":
        with col2:
            k=st.selectbox("List of routes",punjab)
        
        #CREATE A FUNCTION FOR CONNNECTION TO SQL FILTERATION
        
        def type_and_fare(bus_type, fare_range,rate_range):
            conn=pymysql.connect(host="127.0.0.1",user="root",password="Chennai28&",database="vazhai",port=3306)
            my_cursor=conn.cursor()
            
            #filtration for rating
            rate_min, rate_max = 0, 5  # Default range
            if rate_range == 5:
                rate_min, rate_max = 4.1, 5
            elif rate_range == 4:
                rate_min, rate_max = 3.1, 4.0
            elif rate_range == 3:
                rate_min, rate_max = 2.1, 3.0
            elif rate_range == 2:
                rate_min, rate_max = 1.1, 2.0
            elif rate_range == 1:
                rate_min, rate_max = 0, 1.0
                #filteration for fare,bustype and rating
            
            
            #define bus type condition
            if bus_type=="sleeper":
                bus_type_option = "bustype LIKE '%Sleeper%'"
            elif bus_type=="semi-sleeper":
                bus_type_option = "bustype LIKE '%Semi Sleeper %'"
            elif bus_type=="A/C":
                bus_type_option = "bustype LIKE '% A/C %'"
            elif bus_type=="NON A/C":
                bus_type_option = "bustype LIKE '% NON A/C% '"
            elif bus_type=="seater":
                bus_type_option = "bustype LIKE '% Seater %'"
            else:
                bus_type_option = "bustype NOT LIKE '%Sleeper' AND bustype NOT LIKE '%Semi-Sleeper %' AND bustype NOT LIKE '% Seater %' AND bustype NOT LIKE '% A/C%' AND bustype NOT LIKE '%NON A/C %'"
            
            sqlquery= f""" 
                SELECT * FROM busdetail
                WHERE price <= {fare}
                AND route_name = '{k}' 
                AND {bus_type_option} AND start_time >= '{TIME}'
                AND star_rating BETWEEN {rate_min} and {rate_max}
                ORDER BY price and start_time DESC
            """
            
            my_cursor.execute(sqlquery)
            out2=my_cursor.fetchall()
            conn.close()
            
            df=pd.DataFrame(out2,columns=[
                "ID","Bus_name","Bus_type","Start_time","End_time","Duration","Price","Seats_Available","Ratings","Route_link","Route_name"
            ])
            
            return df
        df_result2 = type_and_fare(select_type,fare,select_rating)
        st.subheader("""
                    :blue[:material/resume:] :green[Result]
                    """)
        st.dataframe(df_result2,use_container_width=True)
    
    #ASSAM
    
    if state=="Assam":
        with col2:
           k=st.selectbox("List of routes",assam)
        
        #CREATE A FUNCTION FOR CONNNECTION TO SQL FILTERATION
        
        def type_and_fare(bus_type, fare_range,rate_range):
            conn=pymysql.connect(host="127.0.0.1",user="root",password="Chennai28&",database="vazhai",port=3306)
            my_cursor=conn.cursor()
            
            #filtration for rating
            rate_min, rate_max = 0, 5  # Default range
            if rate_range == 5:
                rate_min, rate_max = 4.2, 5
            elif rate_range == 4:
                rate_min, rate_max = 3.0, 4.2
            elif rate_range == 3:
                rate_min, rate_max = 2.0, 3.0
            elif rate_range == 2:
                rate_min, rate_max = 1.0, 2.0
            elif rate_range == 1:
                rate_min, rate_max = 0, 1.0
                #filteration for fare,bustype and rating
            
            
            #define bus type condition
            if bus_type=="sleeper":
                bus_type_option = "bustype LIKE '%Sleeper%'"
            elif bus_type=="semi-sleeper":
                bus_type_option = "bustype LIKE '%Semi Sleeper %'"
            elif bus_type=="A/C":
                bus_type_option = "bustype LIKE '% A/C %'"
            elif bus_type=="NON A/C":
                bus_type_option = "bustype LIKE '% NON A/C% '"
            elif bus_type=="seater":
                bus_type_option = "bustype LIKE '% Seater %'"
            else:
                bus_type_option = "bustype NOT LIKE '%Sleeper' AND bustype NOT LIKE '%Semi-Sleeper %' AND bustype NOT LIKE '% Seater %' AND bustype NOT LIKE '% A/C%' AND bustype NOT LIKE '%NON A/C %'"
            
            sqlquery= f""" 
                SELECT * FROM busdetail
                WHERE price <= {fare}
                AND route_name = '{k}' 
                AND {bus_type_option} AND start_time >= '{TIME}'
                AND star_rating BETWEEN {rate_min} and {rate_max}
                ORDER BY price and start_time DESC
            """
            
            my_cursor.execute(sqlquery)
            out=my_cursor.fetchall()
            conn.close()
            
            df=pd.DataFrame(out,columns=[
                "ID","Bus_name","Bus_type","Start_time","End_time","Duration","Price","Seats_Available","Ratings","Route_link","Route_name"
            ])
            
            return df
        df_result = type_and_fare(select_type,fare,select_rating)
        st.subheader("""
                    :blue[:material/resume:] :green[Result]
                    """)
        st.dataframe(df_result,use_container_width=True)
        
        
        #TELANGANA
    
    if state=="Telangana":
        with col2:
           k=st.selectbox("List of routes",telangana)
        
        #CREATE A FUNCTION FOR CONNNECTION TO SQL FILTERATION
        
        def type_and_fare(bus_type, fare_range,rate_range):
            conn=pymysql.connect(host="127.0.0.1",user="root",password="Chennai28&",database="vazhai",port=3306)
            my_cursor=conn.cursor()
            
            #filtration for rating
            rate_min, rate_max = 0, 5  # Default range
            if rate_range == 5:
                rate_min, rate_max = 4.2, 5
            elif rate_range == 4:
                rate_min, rate_max = 3.0, 4.2
            elif rate_range == 3:
                rate_min, rate_max = 2.0, 3.0
            elif rate_range == 2:
                rate_min, rate_max = 1.0, 2.0
            elif rate_range == 1:
                rate_min, rate_max = 0, 1.0
                #filteration for fare,bustype and rating
            
            
            #define bus type condition
            if bus_type=="sleeper":
                bus_type_option = "bustype LIKE '%Sleeper%'"
            elif bus_type=="semi-sleeper":
                bus_type_option = "bustype LIKE '%Semi Sleeper %'"
            elif bus_type=="A/C":
                bus_type_option = "bustype LIKE '% A/C %'"
            elif bus_type=="NON A/C":
                bus_type_option = "bustype LIKE '% NON A/C% '"
            elif bus_type=="seater":
                bus_type_option = "bustype LIKE '% Seater %'"
            else:
                bus_type_option = "bustype NOT LIKE '%Sleeper' AND bustype NOT LIKE '%Semi-Sleeper %' AND bustype NOT LIKE '% Seater %' AND bustype NOT LIKE '% A/C%' AND bustype NOT LIKE '%NON A/C %'"
            
            sqlquery= f""" 
                SELECT * FROM busdetail
                WHERE price <= {fare}
                AND route_name = '{k}' 
                AND {bus_type_option} AND start_time >= '{TIME}'
                AND star_rating BETWEEN {rate_min} and {rate_max}
                ORDER BY price and start_time DESC
            """
            
            my_cursor.execute(sqlquery)
            out=my_cursor.fetchall()
            conn.close()
            
            df=pd.DataFrame(out,columns=[
                "ID","Bus_name","Bus_type","Start_time","End_time","Duration","Price","Seats_Available","Ratings","Route_link","Route_name"
            ])
            
            return df
        df_result = type_and_fare(select_type,fare,select_rating)
        st.subheader("""
                    :blue[:material/resume:] :green[Result]
                    """)
        st.dataframe(df_result,use_container_width=True)
    
    
    #HARYANA
    if state=="Haryana":
        with col2:
           k=st.selectbox("List of routes",haryana)
        
        #CREATE A FUNCTION FOR CONNNECTION TO SQL FILTERATION
        
        def type_and_fare(bus_type, fare_range,rate_range):
            conn=pymysql.connect(host="127.0.0.1",user="root",password="Chennai28&",database="vazhai",port=3306)
            my_cursor=conn.cursor()
            
            #filtration for rating
            rate_min, rate_max = 0, 5  # Default range
            if rate_range == 5:
                rate_min, rate_max = 4.1, 5
            elif rate_range == 4:
                rate_min, rate_max = 3.1, 4.0
            elif rate_range == 3:
                rate_min, rate_max = 2.1, 3.0
            elif rate_range == 2:
                rate_min, rate_max = 1.1, 2.0
            elif rate_range == 1:
                rate_min, rate_max = 0, 1.0
                #filteration for fare,bustype and rating
            
            
            #define bus type condition
            if bus_type=="sleeper":
                bus_type_option = "bustype LIKE '%Sleeper%'"
            elif bus_type=="semi-sleeper":
                bus_type_option = "bustype LIKE '%Semi Sleeper %'"
            elif bus_type=="A/C":
                bus_type_option = "bustype LIKE '% A/C %'"
            elif bus_type=="NON A/C":
                bus_type_option = "bustype LIKE '% NON A/C% '"
            elif bus_type=="seater":
                bus_type_option = "bustype LIKE '% Seater %'"
            else:
                bus_type_option = "bustype NOT LIKE '%Sleeper' AND bustype NOT LIKE '%Semi-Sleeper %' AND bustype NOT LIKE '% Seater %' AND bustype NOT LIKE '% A/C%' AND bustype NOT LIKE '%NON A/C %'"
            
            sqlquery= f""" 
                SELECT * FROM busdetail
                WHERE price <= {fare}
                AND route_name = '{k}' 
                AND {bus_type_option} AND start_time >= '{TIME}'
                AND star_rating BETWEEN {rate_min} and {rate_max}
                ORDER BY price and start_time DESC
            """
            
            my_cursor.execute(sqlquery)
            out=my_cursor.fetchall()
            conn.close()
            
            df=pd.DataFrame(out,columns=[
                "ID","Bus_name","Bus_type","Start_time","End_time","Duration","Price","Seats_Available","Ratings","Route_link","Route_name"
            ])
            
            return df
        df_result = type_and_fare(select_type,fare,select_rating)
        st.subheader("""
                    :blue[:material/resume:] :green[Result]
                    """)
        st.dataframe(df_result,use_container_width=True)
        
        
        #GOA 
        
    if state=="Goa":
        with col2:  
          k=st.selectbox("List of routes",goa)
        
        #CREATE A FUNCTION FOR CONNNECTION TO SQL FILTERATION
        
        def type_and_fare(bus_type, fare_range,rate_range):
            conn=pymysql.connect(host="127.0.0.1",user="root",password="Chennai28&",database="vazhai",port=3306)
            my_cursor=conn.cursor()
            
            #filtration for rating
            rate_min, rate_max = 0, 5  # Default range
            if rate_range == 5:
                rate_min, rate_max = 4.1, 5
            elif rate_range == 4:
                rate_min, rate_max = 3.1, 4.0
            elif rate_range == 3:
                rate_min, rate_max = 2.1, 3.0
            elif rate_range == 2:
                rate_min, rate_max = 1.0, 2.0
            elif rate_range == 1:
                rate_min, rate_max = 0, 1.0
                #filteration for fare,bustype and rating
            
            
            #define bus type condition
            if bus_type=="sleeper":
                bus_type_option = "bustype LIKE '%Sleeper%'"
            elif bus_type=="semi-sleeper":
                bus_type_option = "bustype LIKE '%Semi Sleeper %'"
            elif bus_type=="A/C":
                bus_type_option = "bustype LIKE '% A/C %'"
            elif bus_type=="NON A/C":
                bus_type_option = "bustype LIKE '% NON A/C% '"
            elif bus_type=="seater":
                bus_type_option = "bustype LIKE '% Seater %'"
            else:
                bus_type_option = "bustype NOT LIKE '%Sleeper' AND bustype NOT LIKE '%Semi-Sleeper %' AND bustype NOT LIKE '% Seater %' AND bustype NOT LIKE '% A/C%' AND bustype NOT LIKE '%NON A/C %'"
            
            sqlquery= f""" 
                SELECT * FROM busdetail
                WHERE price <= {fare}
                AND route_name = '{k}' 
                AND {bus_type_option} AND start_time >= '{TIME}'
                AND star_rating BETWEEN {rate_min} and {rate_max}
                ORDER BY price and start_time DESC
            """
            
            my_cursor.execute(sqlquery)
            out=my_cursor.fetchall()
            conn.close()
            
            df=pd.DataFrame(out,columns=[
                "ID","Bus_name","Bus_type","Start_time","End_time","Duration","Price","Seats_Available","Ratings","Route_link","Route_name"
            ])
            
            return df
        df_result = type_and_fare(select_type,fare,select_rating)
        st.subheader("""
                    :blue[:material/resume:] :green[Result]
                    """)
        st.dataframe(df_result,use_container_width=True)
    
    
    #RAJASTHAN
    if state=="Rajasthan":
        with col2:
           k=st.selectbox("List of routes",rajasthan)
        
        #CREATE A FUNCTION FOR CONNNECTION TO SQL FILTERATION
        
        def type_and_fare(bus_type, fare_range,rate_range):
            conn=pymysql.connect(host="127.0.0.1",user="root",password="Chennai28&",database="vazhai",port=3306)
            my_cursor=conn.cursor()
            
            #filtration for rating
            rate_min, rate_max = 0, 5  # Default range
            if rate_range == 5:
                rate_min, rate_max = 4.1, 5
            elif rate_range == 4:
                rate_min, rate_max = 3.1, 4.0
            elif rate_range == 3:
                rate_min, rate_max = 2.1, 3.0
            elif rate_range == 2:
                rate_min, rate_max = 1.1, 2.0
            elif rate_range == 1:
                rate_min, rate_max = 0, 1.0
                #filteration for fare,bustype and rating
            
            
            #define bus type condition
            if bus_type=="sleeper":
                bus_type_option = "bustype LIKE '%Sleeper%'"
            elif bus_type=="semi-sleeper":
                bus_type_option = "bustype LIKE '%Semi Sleeper %'"
            elif bus_type=="A/C":
                bus_type_option = "bustype LIKE '% A/C %'"
            elif bus_type=="NON A/C":
                bus_type_option = "bustype LIKE '% NON A/C% '"
            elif bus_type=="seater":
                bus_type_option = "bustype LIKE '% Seater %'"
            else:
                bus_type_option = "bustype NOT LIKE '%Sleeper' AND bustype NOT LIKE '%Semi-Sleeper %' AND bustype NOT LIKE '% Seater %' AND bustype NOT LIKE '% A/C%' AND bustype NOT LIKE '%NON A/C %'"
            
            sqlquery= f""" 
                SELECT * FROM busdetail
                WHERE price <= {fare}
                AND route_name = '{k}' 
                AND {bus_type_option} AND start_time >= '{TIME}'
                AND star_rating BETWEEN {rate_min} and {rate_max}
                ORDER BY price and start_time DESC
            """
            
            
            my_cursor.execute(sqlquery)
            out=my_cursor.fetchall()
            conn.close()
            
            df=pd.DataFrame(out,columns=[
                "ID","Bus_name","Bus_type","Start_time","End_time","Duration","Price","Seats_Available","Ratings","Route_link","Route_name"
            ])
            
            return df
        df_result = type_and_fare(select_type,fare,select_rating)
        st.subheader("""
                    :blue[:material/resume:] :green[Result]
                    """)
        st.dataframe(df_result,use_container_width=True)
    
    
    #UTTAR PRADESH
    if state=="Uttar Pradesh":
        with col2:
           k=st.selectbox("List of routes",up)
        
        #CREATE A FUNCTION FOR CONNNECTION TO SQL FILTERATION
        
        def type_and_fare(bus_type, fare_range,rate_range):
            conn=pymysql.connect(host="127.0.0.1",user="root",password="Chennai28&",database="vazhai",port=3306)
            my_cursor=conn.cursor()
            
            #filtration for rating
            rate_min, rate_max = 0, 5  # Default range
            if rate_range == 5:
                rate_min, rate_max = 4.1, 5
            elif rate_range == 4:
                rate_min, rate_max = 3.1, 4.0
            elif rate_range == 3:
                rate_min, rate_max = 2.1, 3.0
            elif rate_range == 2:
                rate_min, rate_max = 1.1, 2.0
            elif rate_range == 1:
                rate_min, rate_max = 0, 1.0
                #filteration for fare,bustype and rating
            
            
            #define bus type condition
            if bus_type=="sleeper":
                bus_type_option = "bustype LIKE '%Sleeper%'"
            elif bus_type=="semi-sleeper":
                bus_type_option = "bustype LIKE '%Semi Sleeper %'"
            elif bus_type=="A/C":
                bus_type_option = "bustype LIKE '% A/C %'"
            elif bus_type=="NON A/C":
                bus_type_option = "bustype LIKE '% NON A/C% '"
            elif bus_type=="seater":
                bus_type_option = "bustype LIKE '% Seater %'"
            else:
                bus_type_option = "bustype NOT LIKE '%Sleeper' AND bustype NOT LIKE '%Semi-Sleeper %' AND bustype NOT LIKE '% Seater %' AND bustype NOT LIKE '% A/C%' AND bustype NOT LIKE '%NON A/C %'"
            
            sqlquery= f""" 
                SELECT * FROM busdetail
                WHERE price <= {fare}
                AND route_name = '{k}' 
                AND {bus_type_option} AND start_time >= '{TIME}'
                AND star_rating BETWEEN {rate_min} and {rate_max}
                ORDER BY price and start_time DESC
            """
            
            
            my_cursor.execute(sqlquery)
            out=my_cursor.fetchall()
            conn.close()
            
            df=pd.DataFrame(out,columns=[
                "ID","Bus_name","Bus_type","Start_time","End_time","Duration","Price","Seats_Available","Ratings","Route_link","Route_name"
            ])
            
            return df
        df_result = type_and_fare(select_type,fare,select_rating)
        st.subheader("""
                    :blue[:material/resume:] :green[Result]
                    """)
        st.dataframe(df_result,use_container_width=True)
        
    #SOUTH BENGAL 
    if state=="South Bengal":
        with col2:   
           k=st.selectbox("List of routes",sbengal)
        
        #CREATE A FUNCTION FOR CONNNECTION TO SQL FILTERATION
        
        def type_and_fare(bus_type, fare_range,rate_range):
            conn=pymysql.connect(host="127.0.0.1",user="root",password="Chennai28&",database="vazhai",port=3306)
            my_cursor=conn.cursor()
            
            #filtration for rating
            rate_min, rate_max = 0, 5  # Default range
            if rate_range == 5:
                rate_min, rate_max = 4.1, 5
            elif rate_range == 4:
                rate_min, rate_max = 3.1, 4.0
            elif rate_range == 3:
                rate_min, rate_max = 2.1, 3.0
            elif rate_range == 2:
                rate_min, rate_max = 1.1, 2.0
            elif rate_range == 1:
                rate_min, rate_max = 0, 1.0
                #filteration for fare,bustype and rating
            
            
            #define bus type condition
            if bus_type=="sleeper":
                bus_type_option = "bustype LIKE '%Sleeper%'"
            elif bus_type=="semi-sleeper":
                bus_type_option = "bustype LIKE '%Semi Sleeper %'"
            elif bus_type=="A/C":
                bus_type_option = "bustype LIKE '% A/C %'"
            elif bus_type=="NON A/C":
                bus_type_option = "bustype LIKE '% NON A/C% '"
            elif bus_type=="seater":
                bus_type_option = "bustype LIKE '% Seater %'"
            else:
                bus_type_option = "bustype NOT LIKE '%Sleeper' AND bustype NOT LIKE '%Semi-Sleeper %' AND bustype NOT LIKE '% Seater %' AND bustype NOT LIKE '% A/C%' AND bustype NOT LIKE '%NON A/C %'"
            
            sqlquery= f""" 
                SELECT * FROM busdetail
                WHERE price <= {fare}
                AND route_name = '{k}' 
                AND {bus_type_option} AND start_time >= '{TIME}'
                AND star_rating BETWEEN {rate_min} and {rate_max}
                ORDER BY price and start_time DESC
            """
            
            
            my_cursor.execute(sqlquery)
            out=my_cursor.fetchall()
            conn.close()
            
            df=pd.DataFrame(out,columns=[
                "ID","Bus_name","Bus_type","Start_time","End_time","Duration","Price","Seats_Available","Ratings","Route_link","Route_name"
            ])
            
            return df
        df_result = type_and_fare(select_type,fare,select_rating)
        st.subheader("""
                    :blue[:material/resume:] :green[Result]
                    """)
        st.dataframe(df_result,use_container_width=True)
    
    
    
    #WEST BENGAL
    if state=="West Bengal":
        with col2:
           k=st.selectbox("List of routes",wbengal)
        
        #CREATE A FUNCTION FOR CONNNECTION TO SQL FILTERATION
        
        def type_and_fare(bus_type, fare_range,rate_range):
            conn=pymysql.connect(host="127.0.0.1",user="root",password="Chennai28&",database="vazhai",port=3306)
            my_cursor=conn.cursor()
            
            #filtration for rating
            
            rate_min, rate_max = 0, 5  # Default range
            if rate_range == 5:
                rate_min, rate_max = 4.1, 5
            elif rate_range == 4:
                rate_min, rate_max = 3.1, 4.0
            elif rate_range == 3:
                rate_min, rate_max = 2.1, 3.0
            elif rate_range == 2:
                rate_min, rate_max = 1.1, 2.0
            elif rate_range == 1:
                rate_min, rate_max = 0, 1.0
                #filteration for fare,bustype and rating
            
            
            #define bus type condition
            if bus_type=="sleeper":
                bus_type_option = "bustype LIKE '%Sleeper%'"
            elif bus_type=="semi-sleeper":
                bus_type_option = "bustype LIKE '%Semi Sleeper %'"
            elif bus_type=="A/C":
                bus_type_option = "bustype LIKE '% A/C %'"
            elif bus_type=="NON A/C":
                bus_type_option = "bustype LIKE '% NON A/C% '"
            elif bus_type=="seater":
                bus_type_option = "bustype LIKE '% Seater %'"
            else:
                bus_type_option = "bustype NOT LIKE '%Sleeper' AND bustype NOT LIKE '%Semi-Sleeper %' AND bustype NOT LIKE '% Seater %' AND bustype NOT LIKE '% A/C%' AND bustype NOT LIKE '%NON A/C %'"
            
            sqlquery= f""" 
                SELECT * FROM busdetail
                WHERE price <= {fare}
                AND route_name = '{k}' 
                AND {bus_type_option} AND start_time >= '{TIME}'
                AND star_rating BETWEEN {rate_min} and {rate_max}
                ORDER BY price and start_time DESC
            """
            
            my_cursor.execute(sqlquery)
            out=my_cursor.fetchall()
            conn.close()
            
            df=pd.DataFrame(out,columns=[
                "ID","Bus_name","Route_name","Bus_type","Start_time","Duration","End_time","Ratings","Price","Seats_Available","Route_link"
            ])
            
            return df
        df_result = type_and_fare(select_type,fare,select_rating)
        st.subheader("""
                    :blue[:material/resume:] :green[Result]
                    """)
        st.dataframe(df_result,use_container_width=True)

        
    #CHANDIGARH
    if state=="Chandigarh":
        with col2:
           k=st.selectbox("List of routes",chandi)
        
        #CREATE A FUNCTION FOR CONNNECTION TO SQL FILTERATION
        
        def type_and_fare(bus_type, fare_range,rate_range):
            conn=pymysql.connect(host="127.0.0.1",user="root",password="Chennai28&",database="vazhai",port=3306)
            my_cursor=conn.cursor()
            
            #filtration for rating
            
            rate_min, rate_max = 0, 5  # Default range
            if rate_range == 5:
                rate_min, rate_max = 4.1, 5
            elif rate_range == 4:
                rate_min, rate_max = 3.1, 4.0
            elif rate_range == 3:
                rate_min, rate_max = 2.1, 3.0
            elif rate_range == 2:
                rate_min, rate_max = 1.1, 2.0
            elif rate_range == 1:
                rate_min, rate_max = 0, 1.0
                #filteration for fare,bustype and rating
            
            
            #define bus type condition
            if bus_type=="sleeper":
                bus_type_option = "bustype LIKE '%Sleeper%'"
            elif bus_type=="semi-sleeper":
                bus_type_option = "bustype LIKE '%Semi Sleeper %'"
            elif bus_type=="A/C":
                bus_type_option = "bustype LIKE '% A/C %'"
            elif bus_type=="NON A/C":
                bus_type_option = "bustype LIKE '% NON A/C% '"
            elif bus_type=="seater":
                bus_type_option = "bustype LIKE '% Seater %'"
            else:
                bus_type_option = "bustype NOT LIKE '%Sleeper' AND bustype NOT LIKE '%Semi-Sleeper %' AND bustype NOT LIKE '% Seater %' AND bustype NOT LIKE '% A/C%' AND bustype NOT LIKE '%NON A/C %'"
            
            sqlquery= f""" 
                SELECT * FROM busdetail
                WHERE price <= {fare}
                AND route_name = '{k}' 
                AND {bus_type_option} AND start_time >= '{TIME}'
                AND star_rating BETWEEN {rate_min} and {rate_max}
                ORDER BY price and start_time DESC
            """
            
            my_cursor.execute(sqlquery)
            out=my_cursor.fetchall()
            conn.close()
            
            df=pd.DataFrame(out,columns=[
                "ID","Bus_name","Bus_type","Start_time","End_time","Duration","Price","Seats_Available","Ratings","Route_link","Route_name"
            ])
            
            return df
        df_result = type_and_fare(select_type,fare,select_rating)
        st.subheader("""
                    :blue[:material/resume:] :green[Result]
                    """)
        st.dataframe(df_result,use_container_width=True)