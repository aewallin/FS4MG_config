# FS4MG_config

Linuxcnc configuration for my 3-axis mill.

* Linuxcnc on Lenovo M720q (i5-8400T, 16 GiB RAM)
* [FS4MG](https://www.cnc-technik-mueller.de/fs4mg/) fixed gantry frame, travels X 330 mm, Y 270 mm, Z 170 mm
* Stepperonline A6-EC servodrives with 400W servos and 17-bit encoders.
    * with 5 mm pitch ballscrews, 26214.4 counts/mm or 0.038 um/count
    * Z motor has brake
    * PWM frequency set to 16 kHz as explained in [motion4sim](https://docs.motion4sim.com/hardware/servo-driver-settings/ethercat/ethercat-drive-support-omc-a6-series)
    * nominal 3000 rpm gives 15 m/min rapids (way faster than needed)
* Beckhoff IO
    * Outputs EL2809
    * Inputs EL1809
* Omron 3G3MX2-A4030-E VFD with 3G3AX-MX2-ECT Ethercat module
    * Spinogy X22 spindle, 3 kW, 400 V, 4-pole, 30 krpm, air-cooled, with HSKC32 taper. 
* Omron G9SA safety-relay with 3-phase contactor for servos and spindle.
* Toolsetter (Z-axis) from [scratchbuilt-designs](https://www.instagram.com/scratchbuilt_designs/)
* GP-800 wireless 3D probe
* LHB04B-6 USB-wired jogwheel with [xhc-whb04b-6](https://linuxcnc.org/docs/stable/html/man/man1/xhc-whb04b-6.1.html)

## Updates

* 2026-11 Ethercat homing-in-the-drive now works with [cia402_homecomp](https://github.com/linuxcnc-ethercat/cia402_homecomp)
    * 2026-11-02 experimental deb-packages `cia402-homecomp_0.1.0~test2+linuxcnc2.9.10_amd64.deb` and `linuxcnc-ethercat_1.48.0-1-g6654f39+ci_debian-13_amd64.deb`
* Servo tuning using 'servo-tune.py' from [biber-ethercat](https://github.com/shulter/biber-ethercat) works. (alternatively over USB-cable to drive and Windows software)
    * save tuned values to EEPROM with: (the -p argument is the ethercat slave number for the drive)
    * `ethercat download -p 5 0x1010 1 0x73617665 --type uint32`
    * `ethercat download -p 6 0x1010 1 0x73617665 --type uint32`
    * `ethercat download -p 7 0x1010 1 0x73617665 --type uint32`
* jogging all axes from AXIS and jogwheel works

## Linuxcnc install

* 6.12.107+deb13-rt-amd64 #1 SMP PREEMPT_RT Debian 6.12.107-1 (2026-08-29) x86_64 GNU/Linux
* linuxcnc 2.9.10 from ISO file
* installation based on "Ethercat installation from repositories - how to step by step" forum post
* linuxcnc-ethercat from https://linuxcnc-ethercat.github.io/apt/

## Ethercat

* ethercat pdos in file `ethercat_pdos.txt` 
* ethercat sdos in file `ethercat_sdos.txt` 

```
$ ethercat slaves
0  0:0  OP     +  EK1100 EtherCAT-Koppler (2A E-Bus)
1  0:1  OP     +  EL2809 16K. Dig. Ausgang 24V, 0.5A
2  0:2  OP     +  EL2809 16K. Dig. Ausgang 24V, 0.5A
3  0:3  OP     +  EL1809 16K. Dig. Eingang 24V, 3ms
4  0:4  OP     +  EL1809 16K. Dig. Eingang 24V, 3ms
5  0:5  OP     +  AS715N_sAxis_V0.10
6  0:6  OP     +  AS715N_sAxis_V0.10
7  0:7  OP     +  AS715N_sAxis_V0.10
8  0:8  PREOP  +  3G3AX-MX2-ECT EtherCAT Communication Unit for 3G3MX2
```
