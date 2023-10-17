ALL_SERVICES = []

class Service:
    def __init__(self, serviceID: int, serviceName: str, servicePrice: float, 
            serviceDescription: str, serviceTypeID: int):
        global ALL_SERVICES
        self.serviceID = serviceID      # PK
        self.serviceName = serviceName
        self.servicePrice = servicePrice
        self.serviceDescription = serviceDescription
        self.serviceTypeID = serviceTypeID  # FK
        # add service
        ALL_SERVICES.append(self)
        
        
# SERCICETYPE #1 (Haircut)
BasicHaircut = Service(serviceID=1, serviceName='Basic Haircut',
    servicePrice=0, serviceDescription='---', serviceTypeID=1)
CrewCut = Service(serviceID=2, serviceName='Crew Cut',
    servicePrice=0, serviceDescription='---', serviceTypeID=1)
PixieCut = Service(serviceID=3, serviceName='Pixie Cut',
    servicePrice=0, serviceDescription='---', serviceTypeID=1)
LayeredCut = Service(serviceID=4, serviceName='Layered Cut',
    servicePrice=0, serviceDescription='---', serviceTypeID=1)
FadeCut = Service(serviceID=5, serviceName='Fade Cut',
    servicePrice=0, serviceDescription='---', serviceTypeID=1)

# SERVICETYPE #2 (Beard Grooming)
BeardTrim = Service(serviceID=6, serviceName='Beard Trim',
    servicePrice=0, serviceDescription='---', serviceTypeID=2)
BeardShaping = Service(serviceID=7, serviceName='Beard Shaping',
    servicePrice=0, serviceDescription='---', serviceTypeID=2)
BeardColoring = Service(serviceID=8, serviceName='Beard Coloring',
    servicePrice=0, serviceDescription='---', serviceTypeID=2)
HotTowelShave = Service(serviceID=9, serviceName='Hot Towel Shave',
    servicePrice=0, serviceDescription='---', serviceTypeID=2)

# SERVICETYPE #3 (Hair Coloring)
FullHeadColor = Service(serviceID=10, serviceName='Full Head Color',
    servicePrice=0, serviceDescription='---', serviceTypeID=3)
Highlights = Service(serviceID=11, serviceName='Highlights',
    servicePrice=0, serviceDescription='---', serviceTypeID=3)
Balayage = Service(serviceID=12, serviceName='Balayage',
    servicePrice=0, serviceDescription='---', serviceTypeID=3)
RootTouch_Up = Service(serviceID=13, serviceName='Root Touch-Up',
    servicePrice=0, serviceDescription='---', serviceTypeID=3)

# SERVICETYPE #4 (Shaving)
TraditionalStraightRazorShave = Service(serviceID=14, serviceName='Traditional Straight Razor Shave',
    servicePrice=0, serviceDescription='---', serviceTypeID=4)
HotTowelShave = Service(serviceID=15, serviceName='Hot Towel Shave',
    servicePrice=0, serviceDescription='---', serviceTypeID=4)
BeardLineup = Service(serviceID=16, serviceName='Beard Lineup',
    servicePrice=0, serviceDescription='---', serviceTypeID=4)

# SERVICETYPE #5 (Styling)
Blowout = Service(serviceID=17, serviceName='Blowout',
    servicePrice=0, serviceDescription='---', serviceTypeID=5)
StylingWithProduct = Service(serviceID=18, serviceName='Styling with Product',
    servicePrice=0, serviceDescription='---', serviceTypeID=5)
Updo = Service(serviceID=19, serviceName='Updo',
    servicePrice=0, serviceDescription='---', serviceTypeID=5)
Braiding = Service(serviceID=20, serviceName='Braiding',
    servicePrice=0, serviceDescription='---', serviceTypeID=5)


