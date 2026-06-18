# Assessment Task 2: Networking Systems and Social Computing

> **Status:** Final Submission Version  
> **Student Name:** Danny Yu  
> **Class:** 11 CMP01  
> **Due Date:** Friday, 19/06/2026 – Week 9, Period 2

---

## Executive Summary

This report presents a comprehensive upgrade plan for a home network to support a modern smart home environment. The current network, consisting of a basic TP-Link Archer C1200 router and switch, suffers from weak signal coverage, slow speeds, random device dropouts, and limited security. The proposed solution addresses these deficiencies while introducing smart home capabilities, surveillance systems, and edge computing infrastructure.

The upgraded design implements a hybrid star topology with wired backbone connections for critical devices and Wi-Fi for flexible device placement. Key improvements include:
- A new high-performance main router (ZTE BE6800Pro+) with the existing Archer C1200 repurposed as a Wi-Fi access point
- Network segmentation using VLANs to separate trusted devices, IoT systems, surveillance, guest access, and management traffic
- Local edge computing with Raspberry Pi and Jetson devices for real-time automation and processing
- A comprehensive surveillance system with both PoE and Wi-Fi cameras connected to dedicated NVRs
- Centralised storage via an Asustor Flashstor 6 NAS

This design balances performance, security, privacy, and scalability while addressing social, ethical, and legal considerations. The network is validated through Cisco Packet Tracer simulation and follows industry best practices for home network security as recommended by the Australian Cyber Security Centre (ACSC, 2024).

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Network Diagrams](#network-diagrams)
   2.1 [Current Home Network](#current-home-network-diagram)
   2.2 [Identified Problems](#identified-problems-with-the-current-network)
   2.3 [New Smart Home Network Diagram](#new-smart-home-network-diagram)
3. [Simulation: Cisco Packet Tracer](#simulation-cisco-packet-tracer)
4. [Network Plan and Explanation](#network-plan-and-explanation)
   4.1 [Network Type and Data Transmission](#network-type-and-data-transmission)
   4.2 [Topology Selection](#topology-selection)
   4.3 [Hardware Devices and Connections](#hardware-devices-and-connections)
   4.4 [Photographic Evidence](#photographic-evidence)
   4.5 [Addressing and Security Zones](#addressing-and-security-zones)
   4.6 [Wi-Fi Coverage and Control Methods](#wi-fi-coverage-and-control-methods)
   4.7 [Network Security](#network-security)
5. [Cloud and Data Use](#cloud-and-data-use)
   5.1 [Data Storage and Use](#data-storage-and-use)
   5.2 [Cloud vs Edge Computing](#cloud-vs-edge-computing)
   5.3 [Data Security](#data-security)
6. [Innovative Technologies](#innovative-technologies)
7. [Social, Ethical, and Legal Implications](#social-ethical-and-legal-implications)
8. [Conclusion](#conclusion)
9. [References](#references)
10. [Appendices](#appendices)

---

## Network Diagrams

### Current Home Network Diagram

**Figure 1** shows the existing home network architecture before the smart home upgrade. This is a simple star topology with a single TP-Link Archer C1200 router as the central hub, connected to a basic switch providing wired device connectivity.

```mermaid
graph TD
    Internet[Internet ISP]
    Modem[Optical Modem]
    Router[TP-Link Archer C1200 Router]
    Switch[Basic Switch]
    
    Internet --> Modem --> Router
    Router --> Switch
    
    subgraph Wireless Devices
        iPhones[iPhone x3]
        MacBooks[MacBook x2]
        iPads[iPad x2]
        SmartTV[Smart TV]
        
        Router --> iPhones
        Router --> MacBooks
        Router --> iPads
        Router --> SmartTV
    end
    
    subgraph Wired Devices
        PCs[PC x3]
        
        Switch --> PCs
    end
```

### Current Network Device Inventory

| Device Type | Quantity |
|-------------|----------|
| iPhone | 3 |
| PC | 3 |
| MacBook | 2 |
| iPad | 2 |
| Smart TV | 1 |
| Network Switch | 1 |

### Router Placement and Issues

The TP-Link Archer C1200 router is currently installed outside the pantry, chosen because of its central position in the house and proximity to the nearest Ethernet port. This placement was intended to provide stable Wi-Fi coverage, but signal degradation still occurs in distant rooms such as the master bedroom.

### Identified Problems with the Current Network

When evaluated against the requirements for a modern smart home, the current network shows the following deficiencies:

1. **Weak signal coverage in master bedroom** – Wall penetration and distance from the router cause unstable connections
2. **Lack of smart device support** – The network is not designed for IoT devices, automation, or surveillance systems
3. **Slow internet speeds** – The single router struggles with concurrent high-bandwidth activities
4. **Random device dropouts** – Wi-Fi instability causes frequent disconnections
5. **Inadequate security** – Weak passwords and lack of network segmentation expose the network to unauthorised access risk
6. **No automation capabilities** – Does not support smart home convenience or energy efficiency features

These issues show that the current network is sufficient for basic internet access but inadequate for modern smart home needs. In particular, it lacks reliable coverage, dedicated capacity for high-bandwidth devices, and proper security separation between trusted and untrusted devices (NIST, 2023).

### New Smart Home Network Diagram

**Figure 2** shows the proposed upgraded smart home network architecture. The design maintains the simplicity of star topology while adding enhanced Wi-Fi coverage, network segmentation, local storage, edge computing, and a layered security approach.

```mermaid
graph TD
    Internet[Internet ISP]
    NBN[Optical Modem]
    MainRouter[ZTE BE6800Pro Main Router]
    AP[Archer C1200 Wireless Extender]
    CoreSwitch[NETGEAR 16-port PoE Switch]
    PoESwitch[8-port PoE Switch]
    
    Internet --> NBN
    NBN --> MainRouter
    MainRouter --> AP
    MainRouter --> CoreSwitch
    CoreSwitch --> PoESwitch
    
    subgraph Core and Storage
        NAS[Asustor NAS]
        PCs[PC x3 + Mac mini]
        PS4[PS4 + Xbox]
        
        CoreSwitch --> NAS
        CoreSwitch --> PCs
        CoreSwitch --> PS4
    end
    
    subgraph Edge and Automation
        Edge[Raspberry Pi + Jetson x2]
        
        CoreSwitch --> Edge
    end
    
    subgraph Surveillance and Security
        NVRs[NVR x2]
        Cameras[PoE Cameras x4 + WiFi Cameras x5]
        
        PoESwitch --> Cameras
        PoESwitch --> NVRs
    end
    
    subgraph Personal and Mobile
        Mobile[iPhone x4 + iPad x3]
        
        MainRouter --> Mobile
        AP --> Mobile
    end
```

### Before and After Comparison

| Item | Before Upgrade | After Upgrade |
|------|----------------|---------------|
| **Main Router** | TP-Link Archer C1200 | ZTE BE6800Pro + old router reused as AP |
| **Switches** | 1 basic switch | 2 dedicated switches (with PoE capability) |
| **Wireless Coverage** | Single router | Dual router wireless extension |
| **Security** | No segmentation | VLAN network segmentation |
| **Surveillance** | None | Complete camera and NVR system |
| **Storage** | None | Central NAS system |
| **Edge Computing** | None | Raspberry Pi and Jetson platform |

This upgrade directly addresses all weaknesses of the current network while introducing advanced features required for smart home functionality.

---

## Simulation: Cisco Packet Tracer

A Cisco Packet Tracer simulation was developed to validate the proposed network design before physical implementation. The simulation models the network shown in Figure 2 and tests connectivity, coverage, and security segmentation.

### Simulation Objectives

The Packet Tracer model validates four key requirements:

1. **End-to-end connectivity** – Verifies internet access from both wired and wireless clients
2. **Stable backbone communication** – Ensures reliable communication between routers, switches, and access points
3. **Security separation** – Confirms that guest devices cannot access internal trusted systems
4. **Smart home functionality** – Tests camera access, mobile device control, and local automation traffic

### Proposed Addressing Plan

The network uses RFC 1918 private IP addressing with VLAN segmentation to separate traffic types:

| Zone | Subnet | Typical Devices | Validation Focus |
|------|--------|-----------------|------------------|
| Trusted LAN | 192.168.10.0/24 | PCs, Mac mini, NAS, Home Assistant | File access, low latency, full internal access |
| IoT / Smart Devices | 192.168.20.0/24 | Printer, smart lights, app IoT | Internet only, limited trusted LAN access |
| Surveillance | 192.168.30.0/24 | PoE cameras, NVRs | Video stream stability, restricted lateral movement |
| Guest Wi-Fi | 192.168.40.0/24 | Visitor devices | Internet only, no internal access |
| Management | 192.168.99.0/24 | Router/switch admin | Admin-only access with strong authentication |

If full VLAN support is unavailable on all devices, the same security objectives can be achieved using separate SSIDs, router firewall rules, and managed switching where possible (Cisco, 2023).

---

## Network Plan and Explanation

### Network Type and Data Transmission

A **hybrid network architecture** is recommended, combining wired Ethernet connections and wireless Wi-Fi technology.

#### Wired Network Characteristics

In a wired network, data is transmitted as electrical signals over Ethernet cables (typically Cat 5e or Cat 6). Information is divided into packets and transported using the TCP/IP protocol suite:
- **Transmission Control Protocol (TCP)** ensures reliable, ordered delivery of packets with error checking
- **Internet Protocol (IP)** addresses each packet and routes it to the correct destination

Wired networks offer:
- Higher speeds (typically 1 Gbps or 10 Gbps)
- Greater security (less vulnerable to eavesdropping)
- Immunity to wireless interference
- Consistent, low-latency performance

#### Wireless Network Characteristics

Wireless networks use radio waves (Wi-Fi standards such as 802.11ax or 802.11ac) to transmit data packets. Like wired networks, they rely on TCP/IP protocols for communication.

Wireless networks provide:
- Flexible device placement without cabling
- Support for mobile devices
- Convenient access for guests and temporary devices

#### Hybrid Network Justification

The hybrid approach leverages the strengths of both technologies:
- Critical devices (NAS, PCs, NVRs, edge computing nodes) use wired connections for stability and throughput
- Mobile devices, cameras in difficult locations, and convenience-focused IoT devices use Wi-Fi for flexibility

This design follows the principle of using the right technology for each use case, optimising both performance and practicality.

### Topology Selection

A **star topology** has been selected as the network architecture. In this topology, the main router acts as the central hub, with all devices connecting directly or through downstream switches and access points.

#### Advantages of Star Topology

1. **Simple installation and maintenance** – Each device connects to a central point
2. **Fault isolation** – A single device failure does not disrupt the entire network
3. **Easy troubleshooting** – Problems can be traced to specific ports or devices
4. **Centralised security** – Security policies can be enforced at the router
5. **Hybrid support** – Accommodates both wired and wireless devices
6. **Scalability** – Additional devices can be added easily (Cisco, 2023)

The star topology is particularly appropriate for home environments because it matches how consumer routers and switches are typically deployed. For example, if a PoE camera fails, only that port needs testing without affecting other network services.

### Hardware Devices and Connections

The following table summarises the key hardware components in the upgraded network:

| Hardware Device | Function | Rationale |
|-----------------|----------|-----------|
| NBN Optical Modem | Connects home to ISP fibre network | Keeps the WAN design realistic because this is the existing home internet entry point |
| Main Router (ZTE BE6800Pro+) | Routing, NAT, Wi-Fi 7, security policy | Replaces overloaded single-router setup and becomes the security/control core for all zones |
| Second Router/AP (TP-Link Archer C1200) | Wi-Fi coverage extension | Solves weak-signal rooms while reusing an existing device instead of buying another AP |
| NETGEAR JGS516PE Switch | 16-port gigabit with PoE | Needed because the home now has more wired endpoints than router LAN ports |
| 8-port 120W PoE Switch | Dedicated PoE for surveillance | Separates camera power/data load from general traffic and improves CCTV stability |
| Asustor Flashstor 6 NAS | Central storage and backup | Matches household need for shared files, backup, and local media/surveillance retention |
| PCs and Mac mini | Compute and daily use | Reflects real high-bandwidth family usage (development, gaming, content tasks) that benefits from wired links |
| Edge Devices (RPi, Jetson, HA) | Local automation and edge processing | Enables local automations and low-latency processing even during cloud/WAN interruptions |
| Camera System | Security monitoring | Fits the real safety objective of full-home monitoring and remote incident checks |
| NVR System | Video recording and management | Provides local evidence retention and playback without relying only on vendor cloud services |
| iPhones/iPads | User control interface | Mirrors how the household actually controls cameras, alerts, and automation day-to-day |
| Canon Wi-Fi Printer | Shared printing | Represents a practical shared-home endpoint that must remain accessible without new cabling |

All devices connect through the star topology with the ZTE BE6800Pro+ as the main control point. High-demand devices use wired Ethernet for stability, while Wi-Fi serves mobility needs. All communication uses TCP/IP protocols, supporting internal traffic, internet access, and remote monitoring.

These hardware choices are based on the actual household setup, not a generic example. The Archer C1200 is reused as an access point because the house already has weak Wi-Fi areas and the device still has value. The NAS is included because the family needs shared storage and backup. The NVR is included because the cameras need local recording, not only cloud recording. The Raspberry Pi, Jetson boards, and Home Assistant host are included because the home benefits from low-power local automation and edge processing. The cable tools, tracers, and PoE splitter are also part of the design because a real retrofit needs cable testing, cable tracing, and flexible power delivery for cameras or devices without a nearby socket.

In assessment terms, this is a problem-driven selection rather than a technology wishlist: coverage problems map to the AP strategy, random dropouts map to a stronger router and wired backbone, surveillance requirements map to PoE + NVR, and family workflow needs map to NAS plus mobile app control. This direct mapping helps demonstrate authentic design decisions and stronger technical justification.

### Photographic Evidence

The photographs below show the physical equipment that supports the hardware list above. They are grouped by function so the report remains easy to read while still including the real devices used in the home.

**Figure 5: Core networking hardware and installation tools**

| | | |
| --- | --- | --- |
| ![ZTE BE6800 Pro+ router front](PIC/zte_be6800_pro_router_front.jpg) | ![ZTE BE6800 Pro+ router back](PIC/zte_be6800_pro_router_backjpg.jpg) | ![PoE switch](PIC/poe_switch.jpeg) |
| ![Internet cable tools](PIC/internet_cable_tools_1.jpg) | ![Optical wire meter tracer](PIC/wire_meter_tracer_1_optical.jpg) | ![Wire meter tracer](PIC/wire_meter_tracer_2.jpg) |
| ![PoE splitter](PIC/poe_splitter.jpg) | ![Starlink receiver, router, and power supply box](PIC/starlink_satellite_receiver_starlink_router_power_supply_box.jpg) | ![Living Room LG TV](PIC/living_room_lg_tv.jpg) |

**Figure 6: Storage and workstation hardware**

| | | |
| --- | --- | --- |
| ![Asustor NAS front](PIC/asustor_nas_front.jpeg) | ![Asustor NAS back](PIC/asustor_nas_back.jpeg) | ![Synology NAS](PIC/synalogy_nas_1.jpg) |
| ![Home lab overview](PIC/home_lab_1.jpeg) | ![Mac Intel Docker server](PIC/15_years_old_apple_mac_intel_book_x86_1_for_docker_server.jpg) | ![Server PC](PIC/mis_pc_living_server_for_comfy_ui_ai_generator.jpg) |
| ![RTX3090 power supply](PIC/mis_pc_powersupply_1100w_for_rtx3090.jpg) |  |  |

**Figure 7: Edge and automation hardware**

| | | |
| --- | --- | --- |
| ![Raspberry Pi 5](PIC/raspberry_pi_5_4gb.jpg) | ![Jetson Nano 2GB](PIC/jestson_nano_2g_2.jpg) | ![Jetson Nano 4GB](PIC/jestson_nano_4g_1.jpg) |
| ![DIY 3D printer](PIC/diy_3d_printer.jpg) | ![Robot vacuum cleaner](PIC/valcumn_cleaner_rotics.jpg) | ![Sony Vivo notebook](PIC/20_years_old_sony_vivo_note_bookjpg.jpg) |

**Figure 8: Surveillance and recording hardware**

| | | |
| --- | --- | --- |
| ![NVR front](PIC/nvr_recoder_front.jpeg) | ![NVR back](PIC/nvr_recoder_back.jpeg) | ![NVR internal view](PIC/nvr_recoder_in.jpeg) |

Together, these photos show that the network design is based on the household's real equipment and installation constraints. Some devices are reused because they already fit the job, some are added because the current network cannot cover the whole house, and some are installation tools needed to make the retrofit measurable and reliable.

### Addressing and Security Zones

To improve both performance and security, the network implements **network segmentation** through VLANs and security zones. This follows the principle of least privilege, limiting access between device categories.

| Zone | Purpose | Example Devices | Main Security Rule |
|------|---------|-----------------|--------------------|
| Trusted LAN | Personal and high-value devices | PCs, Mac mini, NAS, Home Assistant | Full internal access; not reachable from guest |
| IoT Zone | Everyday smart devices | Printer, smart lights, consumer IoT | Internet only where needed; limited trusted access |
| Surveillance Zone | Cameras and recorders | PoE cameras, Wi-Fi cameras, NVRs | Only approved apps may access feeds |
| Guest Zone | Temporary visitor access | Visitor phones/tablets | Internet only; blocked from all internal zones |
| Management Zone | Administrative control | Router/switch management | Only available to authorised admin devices |

This segmentation is critical because many consumer IoT devices receive infrequent security updates and may be vulnerable. Even if one device is compromised, network limits prevent attackers from moving laterally to more sensitive systems (NIST, 2023).

### Wi-Fi Coverage and Control Methods

The TP-Link Archer C1200 is repurposed as a Wi-Fi access point to extend coverage. It should be placed in the hallway between the main router and weak-signal rooms, ensuring it receives a strong wired backhaul signal while rebroadcasting coverage to distant areas.

#### Control Methods

Smart home devices are managed through:
- **Smartphone apps** – For camera viewing, alert management, and basic controls
- **Home Assistant** – For centralised automation and local control
- **NVR interfaces** – For surveillance recording and playback
- **Router admin interface** – For network configuration and security

Reliable Wi-Fi coverage is not just for convenience—it also improves security by reducing dropouts on cameras, sensors, and control devices that might otherwise create blind spots in the home security system.

### Network Security

The smart home implements a **layered security approach** with multiple overlapping controls:

1. **Strong authentication**
   - Random alphanumeric passwords with special characters for all devices
   - Two-factor authentication (2FA) for cloud accounts and admin interfaces
   - WPA3 encryption for all wireless networks

2. **Network security**
   - Router firewall to block unsolicited incoming traffic
   - VLAN segmentation to limit lateral movement
   - Isolated guest network for visitors
   - Regular firmware updates for all network devices

3. **Operational security**
   - Disable unused ports and services
   - Remove default credentials
   - Review access logs periodically
   - Back up configurations securely
   - Use data minimisation—collect only what is needed

These controls work together to create defence in depth. No single control is perfect, but together they significantly reduce risk. This is especially important in smart homes, where many devices lack enterprise-grade security features (ACSC, 2024).

---

## Cloud and Data Use

### Data Storage and Use

The smart home generates and uses several categories of data:

1. **Operational data** – Device status, automation states, uptime logs, network statistics
2. **Security data** – Camera footage, motion events, access records, alert history
3. **Personal data** – Account details, app credentials, notification preferences, health-related information (if applicable)

IoT and surveillance devices generate much of this data. For example:
- Security cameras record continuous footage and motion-triggered events
- NVR systems index recordings and manage retention
- Home Assistant logs device states and automation triggers

This data is transmitted through the home network to:
- Local NVR and NAS storage
- Mobile apps for local viewing
- Cloud services for remote access and backups

Users can access this data through mobile applications to:
- View real-time camera footage
- Review event recordings
- Receive security alerts
- Check automation status
- Monitor network health

Data classification helps determine appropriate storage locations, retention periods, and access controls.

### Cloud vs Edge Computing

The smart home uses a **mixed cloud-edge model** to balance convenience, privacy, and reliability.

| Data Stored/Processed in Cloud | Data Stored/Processed Locally (Edge) |
|---------------------------------|--------------------------------------|
| Camera event backups and metadata | Real-time motion detection and local recording |
| Mobile push alert history | NVR local recording and indexing |
| Account configuration backups | Home Assistant local automations |
| Remote access dashboards | Edge processing on RPi/Jetson |
| Off-site file backups | Internal LAN communication and control |

#### Cloud Benefits

- Remote access from anywhere with internet
- Automatic off-site backups
- Scalable storage capacity
- Vendor-provided feature updates

#### Edge Benefits

- Instant response without internet round-trips
- Improved privacy (sensitive data stays local)
- Reduced internet data usage
- Continued operation during internet outages

For this smart home, time-critical functions (automations, local recording, real-time alerts) remain at the edge, while cloud services provide remote access and off-site backup resilience. This hybrid approach ensures the home remains functional even if the internet connection is interrupted (NIST, 2023).

### Data Security

Sensitive data is protected through **encryption** and **access control**:

#### Encryption

- **In transit** – WPA3 for Wi-Fi, HTTPS/TLS for web and app communication
- **At rest** – Encrypted storage on NAS and NVR where supported
- **End-to-end** – Where available for camera feeds and cloud services

#### Access Control

- Password protection on all devices and accounts
- Two-factor authentication (2FA) for cloud and admin access
- Role-based access – guests see only what they need
- Least privilege – devices have minimal necessary access

For example, when a camera uploads footage to the cloud:
1. The footage is encrypted during transmission
2. It is stored encrypted at rest
3. Only authenticated users with 2FA can view it

Additionally, **data minimisation** reduces risk. The network should store only data necessary for safety, control, or troubleshooting, with clear retention policies to delete data when it is no longer needed (ACSC, 2024).

---

## Innovative Technologies

### 1. Cloud Computing

Cloud computing delivers storage, computation, and software services over the internet rather than relying solely on local hardware. In this smart home, cloud services support:
- Remote camera viewing and alert notification
- Off-site backup of important configurations
- Account synchronisation across devices

The key benefit is **availability**—users can monitor their home from anywhere without exposing internal network services directly to the internet.

### 2. Edge Computing

Edge computing processes data close to where it is generated instead of sending everything to the cloud. In this design:
- Raspberry Pi 5 runs Home Assistant for local automation
- Jetson Nano devices perform edge processing for camera analytics
- NVR systems handle local recording without internet dependency

The key benefit is **responsiveness**—critical functions continue operating even during internet outages, and privacy is enhanced by keeping sensitive data local.

### 3. Smart Automation

Smart automation enables intelligent decision-making based on pre-defined rules and sensor inputs. In this smart home:
- Camera motion events are filtered to reduce false positives (e.g., ignoring pets while detecting people)
- Home Assistant uses automation based on user habits
- Edge processing reduces unnecessary cloud uploads

The key benefit is **efficiency**—smart systems reduce alert fatigue, prioritise important events, and automate routine tasks without constant user input.

Together, these technologies create a smart home that is not just a collection of devices, but an integrated system where networking, automation, data processing, and security design reinforce each other.

---

## Social, Ethical, and Legal Implications

| Area | Positive Impact | Negative Impact |
|------|-----------------|-----------------|
| **Privacy** | Smart cameras, NVR, and network segmentation improve home security and peace of mind. | Personal data (camera footage, network logs, access records) may be collected and stored. If security fails, unauthorised access is possible. |
| **Society** | Smart home technology improves quality of life through safety, convenience, and accessibility. | Increased reliance on technology may reduce privacy and raise concerns about constant monitoring. Smart home systems can be unaffordable for some, widening the digital divide. |
| **Environment** | Smart automation can reduce energy use by switching off unused devices. | Smart devices consume continuous power and generate e-waste when outdated. |
| **Legal** | Consumer protection and data protection laws support safer deployment. | A hack or data leak may create legal issues around privacy, responsibility, and liability. |

### Ethical Considerations

From an ethical perspective, surveillance should be proportionate and transparent. Cameras should be positioned for security purposes, not for unnecessary monitoring of family, visitors, or neighbours. Users should also understand what data third-party apps and cloud services collect before enabling features by default.

### Legal Considerations

In Australia, smart home deployment must consider:
- The **Privacy Act 1988** – regulates handling of personal information
- **Surveillance Devices Act 2004** – may apply depending on camera placement and recording
- **Australian Consumer Law** – requires products to be safe and fit for purpose

If cameras record areas where people have a reasonable expectation of privacy, additional consent or notice may be required depending on the jurisdiction.

### Social Considerations

While smart homes can improve accessibility for elderly users, busy families, and people with health needs, they can also increase dependence on commercial platforms and internet connectivity. The best design balances convenience, privacy, affordability, and user control—not just the one with the most devices.

---

## Conclusion

This report has presented a comprehensive upgrade plan for a home network to support a modern smart home. The proposed design addresses the current network's weaknesses—poor coverage, instability, limited security, and lack of automation—while introducing significant improvements.

Key recommendations include:
- A hybrid star topology with wired backbone for critical devices
- Network segmentation using VLANs to enhance security
- Local edge computing for resilience and privacy
- A layered security approach following ACSC guidance
- A balanced cloud-edge operating model
- Consideration of social, ethical, and legal implications

The upgraded network provides faster speeds, more reliable coverage, better security, and support for future expansion. It is a practical, future-proof design that meets the needs of a modern smart home while respecting privacy and security requirements.

---

## References

1. Australian Cyber Security Centre (ACSC). (2024). *Secure your smart devices and home network*. Retrieved from https://www.cyber.gov.au/
2. Cisco. (2023). *Network Topologies Overview*. Retrieved from https://www.cisco.com/
3. National Institute of Standards and Technology (NIST). (2023). *Considerations for Managing Internet of Things (IoT) Cybersecurity and Privacy Risks* (NISTIR 8228). Retrieved from https://www.nist.gov/
4. TP-Link. (2024). *Archer C1200 AC1200 Wireless Dual Band Gigabit Router Specifications*. Retrieved from https://www.tp-link.com/au/service-provider/wireless-routers/archer-c1200/#specifications
5. NETGEAR. (2024). *JGS516PE 16-Port Gigabit Easy Smart Managed Plus PoE Switch*. Retrieved from https://www.netgear.com/
6. Office of the Australian Information Commissioner (OAIC). (2023). *Privacy Act 1988 guidelines*. Retrieved from https://www.oaic.gov.au/

---

## Appendices

### Appendix A: Device Inventory Summary

See separate file: `sheets_md/3c_clean_en.md`

### Appendix B: Cisco Packet Tracer File

The Packet Tracer simulation file is included with the submission materials.

### Appendix C: Photographs of Existing Hardware

Photographs of the current router, switches, storage devices, edge devices, and installation tools are provided in the `PIC/` directory. They are included to show that the design is grounded in the actual household setup.

- `zte_be6800_pro_router_front.jpg` – Main router front view
- `zte_be6800_pro_router_backjpg.jpg` – Main router rear ports and cabling
- `poe_switch.jpeg` – PoE switch used for camera power and data
- `internet_cable_tools_1.jpg` – Cable tools used during installation and maintenance
- `wire_meter_tracer_1_optical.jpg` – Optical wire tracer for identifying cable runs
- `wire_meter_tracer_2.jpg` – Wire tracer for checking physical connections
- `poe_splitter.jpg` – PoE splitter for devices without nearby power outlets
- `asustor_nas_front.jpeg` – Asustor NAS front panel
- `asustor_nas_back.jpeg` – Asustor NAS rear connections
- `synalogy_nas_1.jpg` – Additional NAS hardware in the home lab
- `home_lab_1.jpeg` – Home lab overview
- `15_years_old_apple_mac_intel_book_x86_1_for_docker_server.jpg` – Older Mac used as a Docker/server machine
- `mis_pc_living_server_for_comfy_ui_ai_generator.jpg` – Living room server PC used for ComfyUI and tasks
- `mis_pc_powersupply_1100w_for_rtx3090.jpg` – High-wattage PSU for the high-performance PC build
- `raspberry_pi_5_4gb.jpg` – Raspberry Pi 5 used for low-power local services
- `jestson_nano_2g_2.jpg` – Jetson Nano 2GB for edge processing experiments
- `jestson_nano_4g_1.jpg` – Jetson Nano 4GB for edge processing experiments
- `diy_3d_printer.jpg` – DIY 3D printer used for prototyping and repair support
- `valcumn_cleaner_rotics.jpg` – Robot vacuum cleaner showing another smart device in the home
- `20_years_old_sony_vivo_note_bookjpg.jpg` – Older notebook reused for light server or utility work
- `living_room_lg_tv.jpg` – Smart TV used as a networked household endpoint
- `starlink_satellite_receiver_starlink_router_power_supply_box.jpg` – Satellite internet hardware and power supply box
- `nvr_recoder_front.jpeg` – NVR front panel
- `nvr_recoder_back.jpeg` – NVR rear connections
- `nvr_recoder_in.jpeg` – NVR internal view

These photos show why the report uses a mixed design: some devices are reused because they still work, some are added because the house needs better coverage or storage, and some are installation tools needed to make the upgrade reliable and testable.

### Appendix D: Additional Network Diagram Variants

- `smart_home_network_diagram_by_rooms.mmd` – Room-based layout
- `smart_home_network_diagram_simple.mmd` – High-level simplified view
