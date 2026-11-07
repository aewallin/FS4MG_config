# FS4MG_config

Linuxcnc configuration for my 3-axis mill.

* Linuxcnc on Lenovo M720q (i5-8400T, 16 GiB RAM)
    * [linuxcnc-ethercat](https://linuxcnc-ethercat.github.io/linuxcnc-ethercat/)
* [FS4MG](https://www.cnc-technik-mueller.de/fs4mg/) fixed gantry frame, travels X 330 mm, Y 270 mm, Z 170 mm
* Stepperonline A6-EC servodrives with 400W servos and 17-bit encoders.
    * [cia402](https://linuxcnc-ethercat.github.io/linuxcnc-ethercat/cia402.html)
    * with 5 mm pitch ballscrews, 26214.4 counts/mm or 0.038 um/count
    * Z motor has brake
    * PWM frequency set to 16 kHz as explained in [motion4sim](https://docs.motion4sim.com/hardware/servo-driver-settings/ethercat/ethercat-drive-support-omc-a6-series)
    * nominal 3000 rpm gives 15 m/min rapids (way faster than needed)
* Beckhoff EK1100 IO
    * Outputs 2pcs EL2809 ( `lcec.0.1` and `lcec.0.2`)
        * `lcec.0.1.dout-0`: control +24VDC via relay for spindle cooling fan
    * Inputs 2pcs EL1809 ( `lcec.0.3` and `lcec.0.4`)
        * `lcec.0.3.din-0` external e-stop signal from safety-relay, wired to `iocontrol.0.emc-enable-in`
* Omron 3G3MX2-A4030-E VFD with 3G3AX-MX2-ECT Ethercat module
    * [ommx2](https://linuxcnc-ethercat.github.io/linuxcnc-ethercat/ommx2.html), see [#414](https://github.com/linuxcnc-ethercat/linuxcnc-ethercat/issues/414) and [forum post](https://forum.linuxcnc.org/ethercat/56600-omron-mx2#331642)
    * Nominal 400 Hz, max 1000 Hz, max current 6A
    * VFD limited to 580 Hz giving max RPM 17400.
* Spinogy X22 spindle, 3 kW, 400 V, 4-pole, 30 krpm, air-cooled, with HSKC32 taper.
    * pin7 GND cooling fan
    * pin8 +24VDC cooling fan (control via relay)
* Omron G9SA safety-relay with 3-phase contactor for servos and spindle.
* Toolsetter (Z-axis) from [scratchbuilt-designs](https://www.instagram.com/scratchbuilt_designs/)
* GP-800 wireless 3D probe
* LHB04B-6 USB-wired jogwheel with [xhc-whb04b-6](https://linuxcnc.org/docs/stable/html/man/man1/xhc-whb04b-6.1.html)

## Updates

* spindle control both fwd and rev seems to work
* 2026-11 Ethercat homing-in-the-drive now works with [cia402_homecomp](https://github.com/linuxcnc-ethercat/cia402_homecomp)
    * 2026-11-04 `linuxcnc-ethercat_1.48.0-3-gaafe953+ci_debian-13_amd64.deb` and `cia402-homecomp_0.1.0~test3+linuxcnc2.9.10_amd64.deb`
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
