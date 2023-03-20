from datetime import date
from itertools import count
from turtle import color
from PIL import Image
import altair as alt
from pyparsing import White
from sqlalchemy import false
import streamlit as st
import pandas as pd
import plotly.express as px
import streamlit.components.v1 as components 

image2= Image.open('csimage.png')
st.set_page_config(layout = "wide", page_title="CSC 400 | Interactive Dashboard", page_icon = image2)
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

df = pd.read_csv("C:/Users/dillo/OneDrive/Desktop/flows.csv", low_memory=False)
df2 = pd.read_csv("C:/Users/dillo/OneDrive/Desktop/Distributionofattacks.csv", low_memory=False)
df3 = pd.read_csv("C:/Users/dillo/OneDrive/Desktop/allFlows_reduced_withdate.csv", low_memory=False)
df4 = pd.read_csv("C:/Users/dillo/OneDrive/Desktop/allFlows_reduced.csv", low_memory=False)

st.sidebar.title("Real-Time Network Flow DDOS Attacks")
st.sidebar.header("Dillon Alterio Interactive Dashboard")
st.sidebar.write("""Welcome to my interactive dashboard, this dashboard contains a dataframe that consist of DDOS attacks on a real-time universities network. 
                    Every column in the dataframe represents a network flow.  Please choose the selector box to view various charts and graphs pertaining to the dataset below:""")
image = Image.open('ddos.png')
st.sidebar.image(image, caption= 'DDOS ATTACKS ARE NO JOKE!',use_column_width=True)

st.header("Real-Time Network Flow DDOS Attacks")
page = st.sidebar.selectbox('Please Select a Page To View:',
  ['Welcome','Description of Attacks','Distribution of Attacks','All Network Protocol Types Used', 'Network Flow Attack Timeline','Scatter Plot of Packet and Byte Sizes to Attacks'])

if page == 'Welcome':
  components.html("""
                  <html>
                    <style>
                      html {background-color: white;
                            padding:20px;}
                      html {font-family:courier;}
                      h1 {font-size:300%;}
                      p {font-size:150%;}
                    </style>

                    <body>
                      <h1>Welcome to my interactive Dashboard</h1>
                        <p> Attacks on networks are becoming more sophisticated and pose a serious threat to various types of infrastructures. 
                          Unavailability of services due to various forms of DDOS attacks drastically reduces the confidence in the security of that stored data and the ability for a 
                          business/infrastructure to operate efficently.  Throughout this dashboard, the user will be able to view various interactive dashboards that pertain to a real-life 
                          dataset that contains various forms of DDOS attacks.  This dataset includes a ten month timeframe in which network flows were documentated and processed through 
                          the companies custom built IDS(intrusion detection system).  After their IDS processed the network flows, their system indicates what network flows were DDOS 
                          attacks and what network flows were not.  With this information, I was able to create various interactive dashboards that the user will be able to access to gain a better 
                          knowledge on various aspects of DDOS attacks to a real-life network environment.  The user will gain some knowledge in understanding how, when, and through what protocol
                          these malicious acts were conducted in.</p>
                    </body>
                  </html>""", width=1200, height=600,)

if page == 'Description of Attacks':
  components.html("""
                  <html>
                    <style>
                      html {background-color: white;
                            padding:20px;}
                      html {font-family:courier;}
                      h1 {font-size:300%;}
                      p {font-size:150%;}
                    </style>

                    <body>
                      <h1>Description of all DDOS attacks identified on the network:</h1>
                        <p>http_f(HTTP-FLOOD-Attack): </p>
                          <p1>HTTP Flood attacks utilize what appear to be legitimate HTTP GET or POST requests to attack a web server or application. 
                            These flooding DDoS attacks often rely on a botnet, which is a group of Internet-connected computers that have been maliciously appropriated 
                            through the use of malware such as a Trojan Horse. </p1>
                        <p>tcp_syn_f(TCP SYN-Flood-Attack):</p>
                          <p1>How does the TCP SYN flood attack work?
                            A TCP SYN flood DDoS attack occurs when the attacker floods the system with SYN requests in order to overwhelm the target and make it unable to 
                            respond to new real connection requests. It drives all of the target server's communications ports into a half-open state. </p1>
                        <p>tcp_red_w (Code Red Worm): </p>
                          <p1>Code Red is a worm, which is a computer attack that propagates through networks without user intervention. This particular worm makes use of a 
                            vulnerability in Microsoft's Internet Information Services (IIS) Web server software—specifically, a buffer overflow.</p1>
                        <p>udp_f (UDP-Flood-Attack): </p>
                          <p1>A UDP flood is a form of volumetric Denial-of-Service (DoS) attack where the attacker targets and overwhelms random ports on the host with IP 
                            packets containing User Datagram Protocol (UDP) packets.</p1>
                        <p>icmp_smf (Smurf): </p>
                          <p1>A smurf attack is a form of distributed denial-of-service (DDoS) attack that occurs at the network layer. Smurfing attacks are named after the 
                            malware DDoS. Smurf, which enables hackers to execute them.</p1>
                        <p>tcp_land (LAND Attack): </p>
                          <p1> A LAND Attack is a Layer 4 Denial of Service (DoS) attack in which, the attacker sets the source and destination information of a TCP segment 
                            to be the same. A vulnerable machine will crash or freeze due to the packet being repeatedly processed by the TCP stack.</p1>
                        <p>tcp_w32_w (Blaster Worm): </p>
                          <p1>exploits vulnerabilities in the Remote Procedure Call (RPC) Distributed Component Object Model (DCOM) implementation of certain versions of Microsoft Windows. 
                          In addition to performing all of the attributes of a worm such as locating and infecting other hosts, this worm also attempts to conduct a denial-of-service (DOS) 
                            attack on the Microsoft Windows update Web server.</p1>
                        <p>icmp_f (ICMP-Flood): </p>
                          <p1>An Internet Control Message Protocol (ICMP) flood DDoS attack, also known as a Ping flood attack, is a common Denial-of-Service (DoS) attack in which an attacker 
                            attempts to overwhelm a targeted device with ICMP echo-requests (pings).</p1>
                    </body>
                  </html>""", width=1200, height=1250,)
  
if page == 'All Network Protocol Types Used':
 
  clist = df['pr'].unique()
  attack = st.selectbox("Please Select an Attack Protocol Vector:",clist)
  col1, col2 = st.columns(2)

  fig = px.histogram(df[df['pr'] == attack], 
    x = "attack_t", y = "attack_a", color="attack_t", title = 'Attacks aligning with Protocol Type chosen by user:',barmode='group', text_auto=True)
  col1.plotly_chart(fig,use_container_width = True)
  
  fig = px.pie(df[df['pr'] == attack],values='attack_a', names= "attack_t", title = "This pie chart represents the the overall attacks for the Protocol Type: ")
  col2.plotly_chart(fig,use_container_width = True)

if page == 'Network Flow Attack Timeline':
  
  clist1 = df['Monthly'].unique()
  attack = st.selectbox("Please Select Monthly Views of Network Flows containing attacks:",clist1)
  col1, col2 = st.columns(2)
  
  fig = px.histogram(df[df['Monthly'] == attack], 
   x="Monthly", y="attack_a", color="attack_t", title = 'Monthly Attacks on Dataset of selected Month to view:',barmode='group', text_auto=True)
  col1.plotly_chart(fig,use_container_width = True)

  fig = px.pie(df[df['Monthly'] == attack],values='attack_a', names= "attack_t", title = "Pie graph displaying Monthly View of selected Month to view:")
  col2.plotly_chart(fig,use_container_width = True)

  fig = fig = px.scatter(df, x='Monthly', y= ['attack_a','ID'], title="This line graph displays the increase in attacks per month(line-up is increase):")
  col1.plotly_chart(fig,user_container_width = True)

  fig = px.density_heatmap(df, x="Monthly", y="ID", title="Heatmap displays the dataframes contained monthly network flows with attacks:")
  col2.plotly_chart(fig,user_container_width = True)

  clist2 = df['Weekly'].unique()
  attack = st.selectbox("Please Select Weekly Views of Network Flows containing attacks:",clist2)
  col1, col2 = st.columns(2)
  
  fig = px.histogram(df[df['Weekly'] == attack], 
    x = "Weekly", y = "attack_a", color='attack_t', title = 'Weeks Day Attacks on Dataset of selected weekly days to view:',barmode='group', text_auto=True)
  col1.plotly_chart(fig,use_container_width = True)

  fig = px.pie(df[df['Weekly'] == attack],values='attack_a', names= "attack_t", title = "Pie graph displaying Week Days View of selected Month to view:")
  col2.plotly_chart(fig,use_container_width = True)

  fig = fig = px.scatter(df4, x='Weekly', y= ['attack_a','ID'], title="This scatter plot displays week days network flows that have attacks:")
  col1.plotly_chart(fig,user_container_width = True)

  fig = px.density_heatmap(df, x="Weekly", y="ID", title="Heatmap displays the dataframes contained week days network flows with attacks:")
  col2.plotly_chart(fig,user_container_width = True)

  clist3 = df['Daily'].unique()
  attack = st.selectbox("Please Select Daily Views of Network Flows containing attacks:",clist3)
  col1, col2 = st.columns(2)
  
  fig = px.histogram(df[df['Daily'] == attack], 
    x = "Daily", y = "attack_a", color='attack_t', title = 'Daily Attacks on Dataset of selected weekly days to view:',barmode='group', text_auto=True)
  col1.plotly_chart(fig,use_container_width = True)

  fig = px.pie(df[df['Daily'] == attack],values='attack_a', names= "attack_t", title = "Pie graph displaying Daily View of selected Month to view:")
  col2.plotly_chart(fig,use_container_width = True)

  fig = fig = px.scatter(df4, x='Daily', y= ['attack_a','ID'], title="This scatter plot displays daily network flows that have attacks:")
  col1.plotly_chart(fig,user_container_width = True)

  fig = px.density_heatmap(df, x="Daily", y="ID", title="Heatmap displays the dataframes contained daily network flows with attacks:")
  col2.plotly_chart(fig,user_container_width = True)

if page == 'Distribution of Attacks':
  
  clist = df2['Type of Attack'].unique()
  attack = st.selectbox("Select an attack type:",clist)
  col1, col2 = st.columns(2)
  
  fig = px.bar(df2[df2['Type of Attack'] == attack], 
    x='Type of Attack', y=['Network Flows', 'Network Attack Flows'] ,title = 'DDOS Network Flow Attacks on Dataset', text_auto=True)
  col1.plotly_chart(fig,use_container_width = True)
  
  fig = px.pie(df2,values='Network Attack Flows', names= "Type of Attack", title = "This pie chart shows the percentage of all Network Flow(attacks) by attack type", labels='Type of Attack')
  col2.plotly_chart(fig,use_container_width = True)

if page == 'Scatter Plot of Packet and Byte Sizes to Attacks':
  
  clist = df['ID'].unique()
  col1, col2 = st.columns(2)
  
  fig = px.scatter(df4, x="ipkt", y="attack_t", color="attack_a", hover_data=["pr","Date","sending IP","destination IP","ibyt"], title="This scatter plot represents the packet sizes(and other attributes) that were used to attack the network:")
  col1.plotly_chart(fig,user_container_width = True)
