# Assessment Task 2: Networking Systems and Social Computing

## Student Information
- **Name:** Danny Yu
- **Class:** 11 CMP01
- **Due Date:** Friday, 19/06/2026 – Week 9, Period 2

---

## Table of Contents
1. [Network Diagrams](#network-diagrams)
2. [Simulation: Cisco Packet Tracer](#simulation-cisco-packet-tracer)
3. [Network Plan and Explanation](#network-plan-and-explanation)
   - [Network Type](#network-type)
   - [Topology Selection](#topology-selection)
   - [Hardware Devices and Connections](#hardware-devices-and-connections)
   - [Wi-Fi Boosters and Control](#wi-fi-boosters-and-control)
   - [Network Security](#network-security)
4. [Cloud and Data Use](#cloud-and-data-use)
   - [Data Storage and Use](#data-storage-and-use)
   - [Cloud vs Edge Computing](#cloud-vs-edge-computing)
   - [Data Security](#data-security)
5. [Innovative Technologies](#innovative-technologies)
6. [Social, Ethical, and Legal Implications](#social-ethical-and-legal-implications)

---

## Network Diagrams

### Current Home Network Diagram
*Figure 1: Current home network layout placeholder*

### Current Network Device List
- 3 x iPhone
- 3 x PC
- 2 x MacBook
- 2 x iPad
- 1 x Smart TV
- 1 x switch

### Router Placement
The router is installed outside the pantry because this location is central to the house and is close to the nearest Ethernet port. This placement helps provide more consistent Wi-Fi coverage throughout the home.

### Router Specifications
- **Router model:** TP-Link Archer C1200
- **Type:** AC1200 Wireless Dual Band Gigabit Router
- **Source:** https://www.tp-link.com/au/service-provider/wireless-routers/archer-c1200/#specifications

### Identified Problems with the Current Network
- Weak signal in the master bedroom
- No smart devices currently installed
- Slow internet speed
- Devices drop out randomly
- Weak passwords may allow unauthorised access
- No automation for comfort or energy savings

### New Smart Home Network Diagram
*Figure 2: Proposed smart home network diagram placeholder*

---

## Simulation: Cisco Packet Tracer

- The Cisco Packet Tracer simulation file is included in the attachments.

---

## Network Plan and Explanation

### Network Type
A hybrid network architecture is recommended for the smart home.

- **Wired connections:** Use Ethernet cables for stability and speed.
- **Wireless connections:** Use Wi-Fi for flexible placement of smart devices.
- **Data transmission:** TCP/IP protocols divide information into packets and deliver it accurately.

A hybrid network offers the reliability of wired connections and the flexibility of wireless devices.

### Topology Selection
A **star topology** is selected for the smart home network.

- The router is the central hub.
- Devices connect to the router directly via Ethernet or Wi-Fi.

**Advantages of star topology:**
- Easy installation and maintenance
- Reliable operation if one device fails
- Simple troubleshooting
- Centralised security control
- Suitable for wired and wireless devices
- Easy future expansion

### Hardware Devices and Connections

**Table 1: Hardware devices and functions**

**Hardware Device** | **Function** | **Reason it is needed**
--- | --- | ---
Modem | Connects the home network to the ISP | Provides internet access to all devices
Wireless Router (TP-Link Archer C1200) | Manages network traffic and provides Wi-Fi | Central hub for wired and wireless devices
Network Switch | Expands Ethernet ports | Supports additional wired devices such as PCs
Smart Security Cameras | Monitor and record activity | Improve home security through remote viewing
Smart Door Lock | Allows remote locking and unlocking | Increases convenience and access control
Smart Lights | Can be controlled remotely or automated | Improve comfort, convenience, and energy efficiency
Smart Watch (IoMe Device) | Tracks health and activity | Provides personal health monitoring and alerts
Health Monitor (IoMe Device) | Records health metrics | Allows tracking of wellbeing and medical data
Smartphones | Control smart home apps | Primary interface for device management
Laptops / PCs | Manage network and apps | Used for configuration, monitoring, and administration

*Table 1: Hardware devices used in the smart home network.*

All devices connect in a star topology with the wireless router as the central hub. The modem connects to the ISP and links to the router via Ethernet. Wired devices connect through the router or switch, while wireless devices connect via Wi-Fi.

Health devices sync data to a smartphone, which can upload information to cloud services. Smart security cameras stream video through the router to the homeowner's mobile app. The smart door lock and smart lights communicate via the router for remote control.

### Wi-Fi Boosters and Control
The Wi-Fi booster is placed in the hallway between the router and the master bedroom.

- This location extends coverage to distant rooms.
- It strengthens the signal for smart cameras, lights, locks, and health devices.

Smart home devices are controlled using a smartphone app:
- security cameras,
- smart door locks,
- smart lighting,
- smartwatch and health monitor data.

### Network Security
The smart home network uses the following security measures:
- strong passwords,
- WPA3 encryption,
- router firewall protection,
- two-factor authentication (2FA),
- a separate guest Wi-Fi network.

**Security details:**
- Use random alphanumeric passwords with symbols.
- Enable WPA3 to encrypt wireless traffic.
- Configure the router firewall to block suspicious activity.
- Require 2FA for app and cloud access.
- Provide an isolated guest network for visitors.

---

## Cloud and Data Use

### Data Storage and Use
Data from both IoT and IoMe devices is used to improve convenience, security, and wellbeing.

- **IoT devices:** smart cameras, smart door locks, smart lights
- **IoMe devices:** smartwatch, health monitor

**Examples of data use:**
- Camera footage and motion events are stored remotely.
- Door lock activity is recorded for access history.
- Health metrics are uploaded for tracking and analysis.

### Cloud vs Edge Computing

**Table 2: Cloud and edge computing roles**

**Data Stored in the Cloud** | **Data Processed Locally (Edge Computing)**
--- | ---
Smartwatch health history and fitness records | Smart door lock lock/unlock commands
Health monitor backups | Smart light on/off and brightness control
Security camera video recordings | Motion detection processing
Security alerts and notifications | Local device-to-router communication
Smart home settings and preferences | Immediate automation responses

*Table 2: Data storage and processing locations.*

**Cloud computing benefits:**
- remote access,
- automatic backups,
- large storage capacity,
- centralised analytics.

**Edge computing benefits:**
- instant response,
- improved privacy,
- reduced internet usage,
- continued operation during outages.

### Data Security
Sensitive smart home data is protected by encryption and access controls.

- WPA3 secures wireless communication.
- Cloud transfers use encryption.
- Strong passwords are required.
- Two-factor authentication protects accounts.
- Access rights are assigned to authorised users.

**Example:**
- Security camera footage is encrypted in transit and at rest.
- Only authorised users with 2FA can access camera feeds.
- Health data is encrypted and only visible to the account owner.

---

## Innovative Technologies

### 1. Cloud Computing
Cloud computing provides remote storage, processing, and analytics.

- Stores smart home and health data securely.
- Enables remote access through mobile applications.

### 2. Edge Computing
Edge computing processes data locally near the device.

- Improves response time for smart locks and lighting.
- Reduces latency and reliance on internet connectivity.

### 3. Artificial Intelligence (AI)
AI provides smarter device behaviour and insights.

- Security cameras can distinguish people, pets, and vehicles.
- Health devices can analyse data and provide personalised feedback.

These technologies make the smart home more secure, efficient, and user-friendly.

---

## Social, Ethical, and Legal Implications

**Table 3: Impacts of smart home technology**

**Area** | **Positive Impact** | **Negative Impact**
--- | --- | ---
Privacy | Improved home security and wellbeing tracking | Risk of personal data exposure if security fails
Society | Better safety, convenience, and accessibility | Increased surveillance and digital divide concerns
Environment | Energy savings through automation | Continuous power use and electronic waste
Legal | Consumer protection and data laws support safety | Liability if systems are hacked or data is leaked

*Table 3: Social, ethical, and legal implications of smart home systems.*

Smart home technology offers many benefits, but it must be managed carefully to protect privacy, comply with laws, and minimise risk.
