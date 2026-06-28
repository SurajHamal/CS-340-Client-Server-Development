# **CS_340_Client_Server_Development**
This repository contains the portfolio artifacts from CS 340 – Client/Server
Development at Southern New Hampshire University. In this course, I built a
full stack web application dashboard for Grazioso Salvare, an organization that
identifies and trains dogs for search-and-rescue operations. The project
involved importing the Austin Animal Center outcomes dataset into a MongoDB
database, developing a reusable Python CRUD module to handle all database
operations, and building an interactive Dash dashboard that allows users to
filter rescue dog candidates by rescue type — Water, Mountain or Wilderness,
and Disaster or Individual Tracking. The dashboard dynamically updates an
interactive data table, a pie chart showing breed distribution, and a
geolocation map based on the selected filter, following the Model-View-Controller
pattern with MongoDB as the model, Dash as the view, and Python callbacks as
the controller.

# **How do you write programs that are maintainable, readable, and adaptable?**
Throughout this course, I focused on writing code that could be reused across different parts of the project rather than rewriting the same logic repeatedly. The best example of this is the CRUD Python module I built in Project One. By encapsulating all database operations inside a single AnimalShelter class, I was able to import and reuse the same module in the Module Four milestone, the Module Five authentication dashboard, the Module Six milestone, and Project Two — without changing the core database logic each time. This approach follows the principle of separation of concerns, where the database layer is kept completely separate from the presentation layer. The advantages of working this way were significant: when I needed to fix a bug or update authentication, I only had to change one file instead of hunting through multiple notebooks. In the future, this CRUD module could be reused for any application that needs to interact with the AAC dataset, such as a mobile application, a REST API, or a reporting tool, simply by importing the class and calling its methods.

# **How do you approach a problem as a computer scientist?**
When approaching the Grazioso Salvare project, I started by reading the Dashboard Specifications Document carefully to understand exactly what the client needed before writing any code. This top-down approach — understanding requirements first, then designing the solution — helped me avoid building features that didn't meet the client's actual needs. For example, knowing ahead of time that the client needed four specific rescue filters (Water, Mountain, Disaster, and Reset) allowed me to design the MongoDB queries and the dashboard callbacks together, rather than building them separately and hoping they would connect later. This differed from assignments in other courses where the problem was already well-defined and I just needed to implement a known algorithm. Here, I had to translate real-world business requirements into technical specifications. In the future, I would continue this requirements-first approach and also build in more incremental testing — running each filter query in the mongo shell before connecting it to the dashboard — to catch issues earlier in the development process.

# **What do computer scientists do, and why does it matter?**
Computer scientists solve real problems by designing systems that help people work more efficiently and make better decisions. In this project, the work I completed would directly help Grazioso Salvare by replacing a manual, time-consuming process of searching through spreadsheets with an interactive dashboard that filters thousands of animal records in seconds. Instead of a staff member spending hours identifying suitable rescue dog candidates, they can click a single radio button and immediately see a filtered list of dogs that match the breed, sex, and age criteria for a specific type of rescue, along with a map showing where each animal is located. This kind of tool reduces human error, saves time, and allows the organization to focus their resources on training and rescue operations rather than data management. More broadly, this project demonstrates how computer scientists bridge the gap between raw data and meaningful insight — turning a MongoDB database full of shelter records into an actionable decision-making tool for a client doing life-saving work.
