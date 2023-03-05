# D206 Data Cleaning Assessment
## Isaac M. Winters - ID:001311468 - 02/25/2023


### A.  Describe one question or decision that could be addressed using the data set you chose. The summarized question or decision must be relevant to a realistic organizational need or situation.

 - What is the Spaghetti Monsters Nom Nom Nom?

### B. Describe all variables in the data set (regardless of the research question) and indicate the data type for each variable. Use examples from the data set to support your claims.
#### All examples sourced from the first Row of the data set
- Unnamed: 0  - int64 - The ID / Index of the column. - Example: 1
- CaseOrder-  int64 - An index of the original order of the file - Example: 1
- Customer_id  - string - A unique Guid type ID for the patient - Example: C412403
- Interaction - string - A unique Guid type ID for the patient Interaction - Example: 8cd49b13-f45a-4b47-a2bd-173ffa932c2f
- UID - string - Another Guid type ID for the interaction  - Example: 3a83ddb66e2ae73798bdf1d705dc0932
- City - string - The customer city - Example: Eva
- State - string - The customer state - Example: AL
- County - string - The customer county - Example: Morgan
- Zip - int64 - The customer Zip Code - Example: 35621
- Lat - float64 - The latitude of the customer address - Example: 34.34960
- Lng - float64 - The longitude of the customer address - Example: -86.72508
- Population - int64 - Population count within a mile of patient address based on census data - Example: 2951
- Area - string - An area category (rural, urban, or suburban) - Example: Suburban
- Timezone - string - The Verbose description of the timezone - Example: America/Chicago
- Job - string - The career of the patient or primary insured person - Example: Psychologist, sport and exercise
- Children - float64 - Child count in household -  Example: 1.0
- Age - float64 - Patient reported age -  Example: 53.0
- Education - string - Description of patient education - Example: Some College, Less than 1 Year
- Employment - string - Reported employment status -  Example: Full Time
- Income - float64 - Reported annual income - Example: 86575.93	
- Marital - string - Reported marital status - Example: Divorced
- Gender - string - Patients stated gender - Example: Male
- ReAdmission - string - Was the patient readmitted within a month - Example: No
- VitD_levels - float64 - patients vitamin D levels in nanograms per milliliter  - Example: 17.802330
- Doc_visits -  int64 - The count of the visits to the patient by their primary care provider during their initial hospitalization - Example: 6
- Full_meals_eaten - int64 - The number of full meals eaten during hospitalization - Example: 0
- VitD_supp - int64 - Count of vitamin D supplements that were given to the patient - Example: 0
- Soft_drink - string - A flag indication habitual consumption of > 3 soft drinks per day - Example: No *(This example is from row 2, Row 1 is Nan)*
- Initial_admin - string - A description of the type of patient admission method.  - Example: Emergency Admission 
- HighBlood - string - Yes or No for if the patient has high blood pressure - Example: Yes
- Stroke - string - A Yes or No value indicating the patient history of stroke  - Example: No
- Complication_risk - string - A string category value (Low, Medium, High) indicating risk potential - Example: Medium
- Overweight - float64 - A int value indicating if the patient is overweight - Example: 0.0
- Arthritis - string - A Yes or No string value for if the patient has arthritis - Example: Yes
- Diabetes - string - A Yes or No string value for if the patient has diabetes - Example: Yes
- Hyperlipidemia - string - A Yes or No string value for if the patient has hyperlipidemia - Example: No
- BackPain - string - A Yes or No string value for if the patient has back pain - Example: Yes
- Anxiety -  float64 - A 1.0 or 0.0 float value indicating if the patient has an anxiety disorder Example: 1.0
- Allergic_rhinitis - string -  A Yes or No string value for if the patient has allergic rhinitis -  Example: Yes
- Reflux_esophagitis - string - A Yes or No string value for if the patient has reflux espohagitis - Example: No
- Asthma - string - A Yes or No string value for if the patient has asthma - Example: Yes
- Services - string - The string description of the primary service received by the patient - Example: Blood Work	
- Initial_days - float64 - The number of days the patient says at the hospital the first visit - Example: 10.585770
- TotalCharge - float64 - The float value daily charge amount charged to the patient - Example: 3191.048774
- Additional_charges - float64 - The float amount for the avg amount charged to the patient for misc charges - Example: 17939.403420
The following are all survey responses stored as integer. The survey question was: How important is X on a scale from 1 to 8? **8 being low.** 
- Item1 - int64 - Timely admission - Example: 3
- Item2 - int64 - Timely Treatment - Example: 3
- Item3 - int64 - Timely Visits - Example: 2
- Item4 - int64 - Reliability - Example: 2
- Item5 - int64 - Options - Example: 4
- Item6 - int64 - Hours of treatment - Example: 3
- Item7 - int64 - Courteous staff - Example: 3
- Item8 - int64 - Evidence of active listening from the doctors - Example: 4

### C. Explain the plan for cleaning the data by doing the following:
    1. Propose a plan that includes the relevant techniques and specific steps needed to assess the quality of the data 
        in the data set.

    Read that shiz

    2. Justify your approach for assessing the quality of the data, including the following:
        •  characteristics of the data being assessed
            Talk about it yo
        •  the approach used to assess the quality of the data
            Talk more about it yo

    3. Justify your selected programming language and any libraries and packages that will support the data-cleaning process.
        Why we pythoning yo?
        
    4. Provide the annotated code you will use to assess the quality of the data in an executable script file.
        Here's the file

### D.  Summarize the data-cleaning process by doing the following:
    1.  Describe the findings for the data quality issues found from the implementation of the data-cleaning plan from part C.
    2.  Justify your methods for mitigating the data quality issues in the data set.
    3.  Summarize the outcome from the implementation of each data-cleaning step.
    4.  Provide the annotated code you will use to mitigate the data quality issues—including anomalies—in the 
        data set in an executable script file.
    5.  Provide a copy of the cleaned data set as a CSV file.
    6.  Summarize the limitations of the data-cleaning process.
    7.  Discuss how the limitations summarized in part D6 could affect the analysis of the question or decision from part A.

### E.  Apply principal component analysis (PCA) to identify the significant features of the data set by doing the following:
    1.  Identify the total number of principal components and provide the output of the principal components loading matrix.
    2.  Justify the reduced number of the principal components and include a screenshot of a scree plot.
    3.  Describe how the organization would benefit from the use of PCA.

### F.  Provide a Panopto video recording that includes the presenter and a vocalized demonstration of the functionality of the code used for the analysis of the programming environment.

### G.  Acknowledge web sources, using in-text citations and references, for segments of third-party code used to support the application. Be sure the web sources are reliable.

H.  Acknowledge sources, using in-text citations and references, for content that is quoted, paraphrased, or summarized.

I.  Demonstrate professional communication in the content and presentation of your submission.