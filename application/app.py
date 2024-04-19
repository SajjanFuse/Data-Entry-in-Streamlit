import streamlit as st 
import pandas as pd
import os 

# csv paths 
emp_csv = 'employee_data.csv'
depart_csv = 'department_data.csv'

# Check if the CSV file already exists
if not os.path.exists(emp_csv):
    employee_data = pd.DataFrame(columns=['Empno', 'Ename', 'Job', 'Deptno'])
    employee_data.to_csv(emp_csv, index=False)

if not os.path.exists(emp_csv):
    department_data =  pd.DataFrame(columns=['Deptno', 'Dname', 'Loc'])
    department_data.to_csv(emp_csv, index=False)


# using cacne?
@st.cache(allow_output_mutation=True)
def get_employee():
    return []

@st.cache(allow_output_mutation=True)
def get_depart():
    return []


# Employee Data Entry Page
def employee_data_entry():
    st.title('Employee Data Entry')
    
    empno = st.text_input('Employee Number ', '')
    ename = st.text_input('Employee Name ', '')
    job = st.text_input('Job', '')
    deptno = st.text_input('Depart Number ', '')

    if st.button('Submit Employee Data'):
        if empno and ename and job and deptno:
            temp_df = {
                'Empno':empno,
                'Ename':ename,
                'Job':job,
                'Deptno':deptno,
            }

            get_employee().append(temp_df)
            
            
            st.success('Employee data submitted successfully!')

        else:
            st.error('Fill in all the fields.')
    st.dataframe(pd.DataFrame(get_employee()))

# for the departs entry
def department_data_entry():
    deptno = st.text_input('Depart Number ', '')
    dname = st.text_input('Depart Name ', '')
    loc = st.text_input('Location', '')

    if st.button('Submit Depart Data'):
        if deptno and dname and loc:
            temp_df = {
                'Deptno':deptno,
                'Dname':dname,
                'Loc':loc
            }

            get_depart().append(temp_df)

            st.success('Depart data submitted successfully!')
        else:
            st.error('Fill in all the fields.')
    st.dataframe(pd.DataFrame(get_depart()))
    

# for showing 
def visualization():
    
    depart_df = pd.DataFrame(get_depart())
    print(type(depart_df), '\n')
    st.title('Depart Data')
    st.dataframe(depart_df)
    emp_df = pd.DataFrame(get_employee())
    print(type(emp_df))
    print(f'\n\n{emp_df}\n\n')
    st.title('Depart Data')
    st.dataframe(emp_df)
    st.title('Joined Employee and Depart Data')
    
    combined_df = pd.merge(emp_df, depart_df, on='Deptno', how='inner')
    
    st.dataframe(combined_df)

# Sidebar navigation
app_mode = st.sidebar.selectbox('Select Page', ['Employee Data Entry', 'Depart Data Entry', 'Visualization'])

if app_mode == 'Employee Data Entry':
    employee_data_entry()
elif app_mode == 'Depart Data Entry':
    department_data_entry()
elif app_mode == 'Visualization':
    visualization()
