import matplotlib.pyplot as plt

companies = ['Microsoft','Google','Amazon','IBM','Deloitte','Capgemini','ATOS','Amdocs']
recruitments = [120, 150, 180, 90, 110, 130, 80, 70]

# a) Bar Chart
plt.bar(companies, recruitments)
plt.title("Company Recruitment")
plt.xticks(rotation=45)
plt.show()

# b) Pie Chart
plt.pie(recruitments, labels=companies, autopct='%1.1f%%')
plt.title("Recruitment Share")
plt.show()

# c) Customized Pie Chart
plt.pie(recruitments, labels=companies, autopct='%1.1f%%',
        explode=[0.1,0,0,0,0,0,0,0], shadow=True)
plt.title("Customized Pie Chart")
plt.show()

# d) Doughnut Chart
plt.pie(recruitments, labels=companies)
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.title("Doughnut Chart")
plt.show()

# Comparison IBM & Amdocs
plt.bar(['IBM','Amdocs'], [90,70])
plt.title("IBM vs Amdocs Recruitment")
plt.show()
