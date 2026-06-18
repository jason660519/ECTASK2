# Assessment Task 2
## Networking Systems and Social Computing

**Student Name:** Danny Yu  
**Class:** 11 CMP01  
**Due Date:** Friday, 19/06/2026 – Week 9, Period 2

---

## Model – Network Diagrams

### Current Home Network Diagram
*Diagram placeholder*

### Current Network Device List
- 3 x iPhone
- 3 x PC
- 2 x MacBook
- 2 x iPad
- 1 x Smart TV
- 1 x Switch

### Router placement
The router has been installed outside the pantry because this location is central to the house and close to the nearest Ethernet port. This placement helps provide more consistent Wi-Fi coverage throughout the home.

#### Router specifications
- **Router model:** Archer C1200
- **Type:** AC1200 Wireless Dual Band Gigabit Router
- **Link:** https://www.tp-link.com/au/service-provider/wireless-routers/archer-c1200/#specifications

### Identified problems with the current network
- Weak signal in the master bedroom
- No smart devices
- Slow speed
- Devices drop out randomly
- Potential weakness: weak passwords could allow unauthorised users to gain access to sensitive systems and data
- No smart devices to improve comfort and convenience

### New smart home network diagram
*Diagram placeholder*

---

## Section 2: Simulation – Cisco Packet Tracer

The Cisco Packet Tracer file is included in the attachments.

---

## Section 3: Network Plan and Explanation

### Network type and data transmission

In a wired network, information is transmitted as electrical signals over Ethernet cables. Data is broken into smaller packets and transported using TCP/IP protocols. Transmission Control Protocol (TCP) ensures packets arrive safely, while Internet Protocol (IP) addresses each packet and directs it to the correct destination.

Wired networks are usually:
- faster than wireless networks,
- more secure,
- less affected by interference.

In a wireless network, information is also broken into packets and sent over radio waves using Wi-Fi standards. The router broadcasts and receives data as radio signals. Packets are managed by TCP/IP protocols, allowing devices such as smart cameras, smart lighting, smart door locks, and health monitors to communicate and access the internet.

For this smart home project, a hybrid network architecture is recommended because it offers:
- the reliability and speed of wired connections,
- flexible placement of smart devices without cables.

### Selected topology

A star topology has been selected for the smart home network architecture. The router serves as the central hub, with all devices connecting directly to it either by Ethernet or Wi-Fi.

Star topology is suitable because it provides:
- simple installation and maintenance,
- support for both wired and wireless connections,
- isolation of individual device failures,
- consistent performance,
- compatibility with smart home systems,
- future scalability for additional devices.

### Hardware devices and connections

**Hardware Device** | **Function** | **Reason it is needed**
--- | --- | ---
Modem | Connects the home network to the Internet Service Provider (ISP) | Provides internet access to all devices.
Wireless Router (TP-Link Archer C1200) | Manages network traffic and provides Wi-Fi coverage | Acts as the central hub in the star topology.
Network Switch | Expands the number of Ethernet ports | Enables more wired devices to connect to the network.
Smart Security Cameras | Monitor and record home activity | Improve security with remote viewing capabilities.
Smart Door Lock | Allows remote locking and unlocking | Increases convenience and access control.
Smart Lights | Can be controlled remotely or automated | Improve comfort, energy efficiency, and convenience.
Smart Watch (IoMe Device) | Tracks health and activity | Lets users monitor fitness and receive alerts.
Health Monitor (IoMe Device) | Records health information such as heart rate | Helps users track their health and wellbeing through connected applications.
Smartphones | Control smart home devices through apps | Provide the main method for remote management.
Laptops/PCs | Access network settings, cloud services, and device management platforms | Allow advanced control and configuration of the smart home network.

All devices in the smart home connect using a star topology with the router as the central hub. The modem connects to the ISP and links to the router via Ethernet. The router provides Wi-Fi access to wireless devices, including smart cameras, the smart door lock, smart lights, the smartwatch, the health monitor, smartphones, laptops, and iPads.

The smartwatch and health monitor send health data to a smartphone, which can upload it to cloud services for storage and analysis. Smart security cameras transmit live video to the homeowner's mobile app through the router. The smart door lock communicates with the router for remote lock and unlock control. Smart lights receive commands through the smartphone app for remote lighting control.

All data travels through the router using TCP/IP protocols, enabling communication between devices, cloud access, and real-time smart home functionality. PCs are connected via Ethernet to a switch, while wireless smart devices use the 2.4 GHz Wi-Fi band to maximise signal range.

### Wi-Fi boosters and control methods

A Wi-Fi booster is positioned in the hallway between the router and the master bedroom. This location helps the booster receive a strong signal from the router and extend coverage to other rooms.

IoT devices will be managed primarily through a smartphone app installed on the homeowner's phone. The app will allow the user to:
- manage security cameras,
- open and lock doors,
- control smart lighting,
- access health data from the smartwatch and health monitor.

### Network security

To protect the smart home network, the following security measures will be implemented:
- strong passwords,
- firewall protection,
- two-factor authentication (2FA),
- a guest network for visitors.

Using strong passwords and WPA3 encryption:
- Smart home devices and user accounts will use random alphanumeric passwords with special characters.
- WPA3 will protect wireless communication and encrypted data transmitted across the network.

Using the router firewall:
- the firewall will monitor network traffic,
- suspicious activity, hacking attempts, and malware will be blocked.

Implementing two-factor authentication:
- 2FA will protect user accounts and cloud access,
- users will need both a password and a verification code to sign in.

Guest network:
- an isolated guest Wi-Fi network will be created,
- guests can access the internet without accessing smart home devices or private information.

These security measures help prevent unauthorised access, cyberattacks, and data theft.

---

## Section 4: Cloud and Data Use

### Data storage and use

The smart home collects data from both IoT (Internet of Things) and IoMe (Internet of Me) devices. This data is stored and used to improve convenience, security, and personal wellbeing.

IoT devices such as smart cameras, smart door locks, and smart lights generate activity data. For example:
- security cameras record footage and motion events,
- smart locks record when doors are locked and unlocked.

This data is sent through the home network to mobile apps and cloud servers, where authorised users can access it remotely.

IoMe devices such as a smartwatch and health monitor collect health-related data, including:
- heart rate,
- physical activity,
- sleep patterns,
- fitness achievements.

This data is transferred wirelessly to a smartphone and uploaded to the cloud.

Users can access cloud data through mobile applications to monitor home activity and health information. For example, a homeowner can:
- view real-time camera footage,
- check door lock status,
- control smart lighting,
- review smartwatch health data.

### Cloud vs edge computing

**Data Stored in the Cloud** | **Data Processed Locally (Edge Computing)**
--- | ---
Smartwatch health history and fitness records | Smart door lock lock/unlock commands
Health monitor backups | Smart light on/off and brightness controls
Security camera video recordings and backups | Motion detection processing by security cameras
Security alerts and notifications | Live communication between devices and the router
Smart home settings and user preferences | Immediate device responses and automation routines

Both cloud computing and edge computing are used in this smart home.

Cloud computing provides:
- remote access,
- automatic backups,
- large storage capacity,
- access from anywhere with an internet connection.

Edge computing provides:
- instant response,
- improved privacy,
- reduced internet data usage,
- continued operation during internet outages.

### Data security examples

Sensitive information on smart home devices is protected using encryption and access control.

Encryption covers wireless communication and cloud transfers. The smart home uses WPA3 encryption for secure wireless connections. Data from the smartwatch, health monitor, smart door lock, and cameras is encrypted during transmission and storage.

Access control restricts access to authorised users. Passwords are required on all devices, and two-factor authentication (2FA) is used for mobile apps and cloud services. 2FA requires a password plus a verification code sent to a phone.

For example, when a security camera uploads footage to the cloud:
- the footage is encrypted in transit and at rest,
- only authorised users with correct credentials and 2FA can view the footage.

Similarly, health data from the smartwatch and health monitor is encrypted and only accessible to the account owner.

Combining encryption and access control protects privacy and reduces the risk of unauthorised access or data breaches.

---

## Innovative Technologies and Their Influence on the Smart Home

### 1. Cloud Computing

Cloud computing provides storage, software, and computation resources over the internet instead of relying on local devices. In the smart home, cloud services store data from the smartwatch, health monitor, cameras, and smart lock. Cloud access enables remote monitoring and analysis through mobile apps.

### 2. Edge Computing

Edge computing processes data close to the source rather than in the cloud. In the smart home, devices such as smart cameras and smart locks can perform local processing. For example, a smart camera can detect movement and notify the homeowner instantly without waiting for cloud processing.

### 3. Artificial Intelligence (AI)

AI helps devices perform tasks that require pattern recognition and decision-making. In the smart home, AI can help cameras distinguish people from pets or vehicles. It can also analyse health data from the smartwatch and health monitor to provide personalised insights.

These technologies make the smart home more secure, convenient, and efficient.

Cloud computing provides storage and remote access. Edge computing enables fast local processing. AI helps devices make smarter decisions.

---

## Social, Ethical, and Legal Implications

**Area** | **Positive Impact** | **Negative Impact**
--- | --- | ---
Privacy | Smart cameras and door locks improve home security and peace of mind. Smartwatches and health monitors help track wellbeing. Smart lights increase convenience and energy efficiency. | Personal data such as health records, camera footage, and access logs may be collected and stored. If security fails, unauthorised users could access sensitive information.
Society | Smart home technology improves quality of life through safety, convenience, and accessibility. Health-monitoring devices support healthier lifestyles and independent living. | Increased reliance on technology may reduce privacy and raise concerns about constant monitoring. Smart home systems can be unaffordable for some people, contributing to a digital divide.
Environment | Smart lights and automation can reduce energy use by switching devices off when not needed. This can lower electricity usage and environmental impact. | Smart devices consume power continuously and generate electronic waste when outdated. Manufacturing devices also uses resources and energy.
Legal | Consumer protection laws help ensure smart home products are safe and reliable. Data protection laws require companies to handle personal information responsibly. | Companies collecting user data must comply with privacy laws. A hack or data leak may lead to legal issues around responsibility and liability.

Smart home networks deliver benefits such as improved security, convenience, and health monitoring through devices like cameras, smart locks, smartwatches, and health monitors. However, they also collect large volumes of personal data, raising privacy concerns if the data is not properly protected.
