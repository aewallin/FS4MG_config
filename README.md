# FS4MG_config

Linuxcnc configuration for my 3-axis mill.

* Linuxcnc on Lenovo M720q (i5-8400T, 16 GiB RAM)
* FS4MG frame (https://www.cnc-technik-mueller.de/fs4mg/)
* Stepperonline A6-EC servodrives with 400W servos and 17-bit encoders.
* Beckhoff IO, EL2809, EL1809
* spindle config TBD

## Updates

* WIP: homign using [cia402_homecomp](https://github.com/rodw-au/cia402_homecomp)
    * state-machine starts HOME_START
    * we get to CUSTOM_BEGIN
    * we get to CUSTOM_INIT
    * we get to CUSTOM_RUNNING
    * Then: joint 0 amplifier fault (drive display Er87.1  "One-time excessive position reference increment")
* Servo tuning using 'servo-tune.py' from [biber-ethercat](https://github.com/shulter/biber-ethercat) works. (alternatively over USB-cable to drive and Windows software)
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
