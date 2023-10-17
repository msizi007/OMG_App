import datetime
from schedule import Schedule


# BUSINESS WORKING HOURS
# Mon-Fri: 9am - 5pm
# Sat: 9am - 3pm
# Sun: Closed

TIME_9AM = datetime.time(9, 0)
TIME_3PM = datetime.time(15, 0)
TIME_5PM = datetime.time(17, 0)

class Appointment:
    def __init__(self, schedule: Schedule, customer_num: int, service_num: int):
        self.schedule = schedule
        self.appointmentDate = None
        self.appointmentTime = None
        self.appointmentStatus = 'Pending!'
        self.customer_num = customer_num
        self.service_num = service_num
    
    def ApproveAppointment(self):
        self.appointmentStatus = "Approved!"



"""
To differentiate between service types and services in your barbershop, you can create a hierarchical structure where each service type can have multiple services associated with it. Here's a breakdown of the concept with examples:

1. Service Types:
   - Service types are broad categories or classifications of the services you offer in your barbershop. Each service type represents a group of related services.
   
   Examples of Service Types:
   - Haircuts
   - Beard Grooming
   - Hair Coloring
   - Shaving
   - Styling

2. Services:
   - Services are specific treatments or procedures that fall under a particular service type. Each service is associated with only one service type.
   
   Examples of Services under the "Haircuts" Service Type:
   - Basic Haircut
   - Crew Cut
   - Pixie Cut
   - Layered Cut
   - Fade Haircut

   Examples of Services under the "Beard Grooming" Service Type:
   - Beard Trim
   - Beard Shaping
   - Beard Coloring
   - Hot Towel Shave

   Examples of Services under the "Hair Coloring" Service Type:
   - Full Head Color
   - Highlights
   - Balayage
   - Root Touch-Up

   Examples of Services under the "Shaving" Service Type:
   - Traditional Straight Razor Shave
   - Hot Towel Shave
   - Beard Lineup

   Examples of Services under the "Styling" Service Type:
   - Blowout
   - Styling with Product
   - Updo
   - Braiding

Each service type groups similar services together, making it easier for your customers to understand the range of services you offer. This hierarchical structure allows you to organize your menu of services more effectively and makes it clear that each service type can contain multiple specific services.

Additionally, this organization can help you set pricing, track inventory (if applicable), and market your services more efficiently. Customers can easily browse through the service types to find the specific service they're interested in, enhancing their overall experience in your barbershop.
"""