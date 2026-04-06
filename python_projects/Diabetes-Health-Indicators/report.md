Project: Can we predict Diabetes from Lifestyle?

the Anlaysis started by checking if the data was "clean" (no missing values) and it looked good. a PatientID was added  to keep track of everyone. Then, the data was simplified: instead of three different types of diabetes,it was summarized to on;y two groups: Healthy and Diabetic.

2. Finding the "Red Flags":
pivot tables were created to see which factors (like BMI, High Blood Pressure, and Smoking, etc...) are different between healthy and sick people, which can help deduce the overall risk of Diabetes .

Intriguing Discovery: It was observed that people who are active have a much lower risk. Specifically, the risk of diabetes is 43.75% lower for people who exercise compared to those who don't.

3. Building the "Risk-Factor" Engine:
Based on the above mentioned Risk categorizes, a 'Risk-Factor' calculator was built.
The objectives of this engine is to quantify the risk of a healthy indivdual developing Diabtes in the future.

Technical Note: I first tried a calculate_risk function with .apply(), but it was way too slow for 250,000 rows. So, I switched to a "vectorized" method which was much faster!

 1 point was given for each bad factor (High BMI, Smoking, no exercise, etc.).

4. Validation of Results:
To see if the scoring was right, people grouped into Low, Medium, and High Risk.

High Risk: About 51% of people in this group have diabetes. It's like a coin flip!

Medium Risk: About 30% have it.

Low Risk: Only about 9% have it.

Conclusion:
The "Risk-Factor" score is functional! If someone has a score higher than 6, they are much more likely to be diabetic.

5. What can be deduced from this analysis and the Risk-Profile?

We should find the "High Risk" people and get them to a doctor fast.

For the "Younger" or "Medium Risk" people, we should encourage them to eat more veggies and exercise, because the data shows that exercise really does lower the risk!

