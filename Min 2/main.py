import pandas as pd
import streamlit as st

df = pd.read_csv('AI_Project.csv')
st.markdown(
    """
    <style>
    /* Add your CSS styles here */
    body {
        background-color: #f0f0f0;
        font-family: Arial, sans-serif;
    }
    h1 {
        color: #333;
    }
    .container {
        padding: 20px;
        background-color: #fff;
        border-radius: 10px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }
    </style>
    """,
    unsafe_allow_html=True
)


df = pd.read_csv('AI_Project.csv')

st.title("Travel Planner Expenses App")


state = st.text_input("Enter the state:")


Filt_state = df[df['State'] == state.title()]

if len(Filt_state) == 0:
    st.write("No data available for the entered state.")
else:
    Categories = Filt_state['Category'].tolist()
    st.write(Filt_state)

    preference = st.text_input("Enter the destination category:")

    if preference.title() in Categories:
        Filt_state = Filt_state[Filt_state['Category'] == preference.title()]
        st.write("These are the available Destinations in " +
                 state + " for " + preference.title())
        st.write(Filt_state)
    else:
        st.write("The entered choice is not available")
        st.write("Choose from below list")
        for i in Categories:
            st.write(i)

    Type_accomodation = st.selectbox("Select accommodation type:", [
                                     'With Food', 'Accomodation'])
    budget = st.number_input(
        "Enter the budget for the trip per day:", min_value=0)

    if Type_accomodation == 'With Food':
        Filt_state1 = Filt_state[Filt_state['With Food'] <= budget]
        flag = "With Food"
        dum = "Accomodation"
    else:
        Filt_state1 = Filt_state[Filt_state['Accomodation'] <= budget]
        flag = "Accomodation"
        dum = "With Food"

    if len(Filt_state1) == 0:
        st.write("There are no available choices within your entered budget.")
        st.write("If you need a trip, increase your budget or change the choices.")
    else:
        sort_column = st.selectbox(
            "Select a column to sort the table:", Filt_state1.columns)
        ascending = st.checkbox("Sort in ascending order")
        Filt_state1 = Filt_state1.sort_values(
            by=sort_column, ascending=ascending)
        st.write(
            "The provided table shows the available choices according to your input")
        st.write(Filt_state1)

    # User_destination = 1
    # user_list = []
    #
    # while User_destination:
    #     User_destination = st.text_input("Enter 0 to stop or choose your favorite destination:")
    #     if User_destination == str(0):
    #         break
    #     user_list.append(User_destination.title())

    User_destination = 1
    user_list = []

    while User_destination:
        User_destination = st.text_input(f"Enter 0 to stop or choose your favorite destination {len(user_list) + 1}:",
                                         key=f"destination_{len(user_list)}")
        if User_destination == str(0):
            break
        user_list.append(User_destination.title())

    sum_total = 0
    user_table = []

    for i in user_list:
        Filt_state2 = Filt_state1[Filt_state1['Destination'] == i]
        Filt_state2 = Filt_state2.loc[:, Filt_state2.columns != dum]
        user_table.append(Filt_state2)

    if len(user_table) > 0:
        st.write("Thank you! The provided table shows all the details:")
        user_table = pd.concat(user_table)
        st.write(user_table)
        sum_total = user_table[flag].sum()
        st.write("The total cost for the following trip is Rs", sum_total)
