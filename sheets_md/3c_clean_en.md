# Home Device Inventory Summary

> Source: normalized from `3c_orig_en.md`. Use this file when you need a readable summary for report writing or diagram cross-checking.

## Purpose

This file is the clean companion to the raw sheet export. It keeps only the device groups and major hardware items that are relevant to the smart home network report.

## Core Network Infrastructure

| Category | Devices |
| --- | --- |
| ISP access | NBN optical modem with 4 UNI-D ports |
| Main router | ZTE BE6800Pro+ |
| Secondary router / AP | TP-Link Archer C1200 |
| Switching | NETGEAR JGS516PE 16-port switch, 8-port 120W PoE switch |
| Cabling | Cat 5e / Cat 6 Ethernet cabling and RJ45 wall ports |

## Core Compute and Storage

| Category | Devices |
| --- | --- |
| NAS | Asustor Flashstor 6 NAS |
| Desktop PCs | PC-1 Dad AMD + RTX3090, PC-2 Younger Brother Intel + RTX5070, PC-3 Brother Intel + RTX3060 |
| Apple device | Mac mini M4 |
| Edge devices | Raspberry Pi 5, Jetson Nano 2GB, Jetson Nano 4GB |
| Home automation host | Asus notebook running Home Assistant |

## Personal and Entertainment Devices

| Category | Devices |
| --- | --- |
| Phones | iPhone devices used by family members |
| Tablets | iPad, iPad mini, iPad Pro |
| Consoles | Sony PS4, Xbox |
| Printer | Canon G3830 / G3832 wireless printer |

## Surveillance and Security Devices

| Category | Devices |
| --- | --- |
| Wi-Fi camera | Tuya 4K Wi-Fi floodlight camera |
| PoE cameras | Xiongmai PoE cameras x4 |
| Wi-Fi cameras | ANNKE Wi-Fi cameras x4 |
| Video recorders | Xiongmai 16-channel NVR, ANNKE 4-channel NVR |

## Notes for Report Use

- Use `3c_orig_en.md` when you need the full raw export history.
- Use this file when you need concise device counts, categories, or cross-check material for `report_draft.md` and Mermaid diagrams.
- If new devices are added to the raw export, update this summary instead of editing report sections from the raw table directly.