
# importing required libraries
import pickle
import streamlit as st

# loading the trained model
pickle_in = open('classifier.pkl', 'rb') 
classifier = pickle.load(pickle_in)

# this is the main function in which we define our app  
def main():       
    # header of the page 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Check your Loan Eligibility</h1> 
    </div> 
    """
    st.markdown(html_temp, unsafe_allow_html = True) 

    # following lines create boxes in which user can enter data required to make prediction 
    Gender        = st.selectbox('Gender',("Male","Female","Other"))
    Married       = st.selectbox('Marital Status',("Unmarried","Married")) 
    Self_Employed = st.selectbox('Self_Employed',("Yes","No")) 
    Dependents    = st.selectbox('Number of Dependents',("0","1", "2", "3+")) 
    Education     = st.selectbox('Education level',("Graduate","Not Graduate")) 
    Property_Area = st.selectbox('Property_Area',("Rural","Semiurban", "Urban")) 
    
    ApplicantIncome   = st.number_input("Monthly Income in Rupees")
    CoapplicantIncome = st.number_input("Coapplicant's Monthly Income in Rupees")
    LoanAmount        = st.number_input("Loan Amount in Rupees")
    Loan_Amount_Term  = st.number_input("Term for Loan Amount")
    Credit_History    = st.number_input("Credit_History")
    
    
    result =""
      
    # when 'Check' is clicked, make the prediction and store it 
    if st.button("Check"): 
        result = prediction(Gender, Married,Self_Employed,Dependents,Education,Property_Area,
                            ApplicantIncome, CoapplicantIncome,LoanAmount,Loan_Amount_Term ,Credit_History) 
        st.success('Your loan is {}'.format(result))
        
# defining the function which will make the prediction using the data which the user inputs 
def prediction(Gender, Married,Self_Employed,Dependents,Education,Property_Area, ApplicantIncome,CoapplicantIncome,
               LoanAmount,Loan_Amount_Term ,Credit_History): 

    # 2. Loading and Pre-processing the data 

    if Gender == "Male":
        Gender = 0
    else:
        Gender = 1

        
    if Married == "Yes":
        Married = 1
    else:
        Married = 0

        
    if Self_Employed == "Yes":
        Self_Employed = 0
    else:
        Self_Employed = 1

    
    if Dependents == "0":
        Dependents = 0
    elif Dependents == "1":
        Dependents = 1
    elif Dependents == "2":
        Dependents = 2
    else:
        Dependents = 3
    
    
    if Education == "Graduate":
        Education = 1
    else:
        Education = 0
    
    
    if Property_Area == "Rural":
        Property_Area = 0
    elif Property_Area=="Semiurban":
        Property_Area = 1
    else:
        Property_Area = 2

    prediction = classifier.predict( 
        [[Gender, Married, Self_Employed,Dependents,Education,Property_Area,ApplicantIncome,CoapplicantIncome,
          LoanAmount,  Loan_Amount_Term,Credit_History ]])
     
    if prediction == 0:
        pred = 'Rejected'
    else:
        pred = 'Approved'
    return pred
 

     
if __name__=='__main__': 
    main()
