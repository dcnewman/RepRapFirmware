*This document details how to build the RepRapFirmware using scons.*
*For documentation on installing and configuring the RepRapFirmware*
*on an RADDS v1.5 board, see the file `doc/RADDS-v1.5.md`*

Traditionally, the Duet RepRapFirmware is built using the Eclipse
IDE.  If that is to your liking, then by all means go ahead and
do so.  However, This fork of the RepRapFirmware may also be built
using the [scons](http://scons.org/) command line tool,

1. Should your system lack Python 2.x, download and install it.

2. Download and install [scons](http://scons.org/).  Version 2.3.5 or
   later is required.

3. Install the [Arduino](https://www.arduino.cc/) application.
   Version 1.5.8beta is known to work.  You will merely be using the
   gcc-arm toolchain installed with/by the Arduino application.
   
4. Run the Arduino application and install the ARM programming tools.
   Look under "Tools > Board > Boards Manager...".  Select the "Arduino
   SAM Boards (32-bits ARM Cortex-M3) by Arduino" and install it.

5. From this github repository, edit the file

       scons_tools/sample_rrf_arduino_paths.py

   as appropriate to indicate the location of your installed gcc-arm
   tool chain and location of the CoreNG sources (Step 6).  Then save
   this file to your home directory as the file

       ~/.rrf_arduino_paths.py
   
6. Obtain and build for RADDS a copy of the github [CoreNG
   repo](https://github.com/dcnewman/CoreNG).

7. From the top-level RepRapFirmware repository directory, build the
   firmware for RADDS with the command

       scons platform=radds
   	     
    Once scons finishes, the resulting files will be in the directory

       build/radds/

   The final build product is the file `RepRapFirmware-radds.bin`.

   To instead build for Duet, omit the "platform=radds" parameter (or
   specify "duet" for the platform name),

       scons

   The resulting `RepRapFirmware-duet.bin` file will then be in
   	     
       build/duet/

8. For boards with a Native Programming Port and the
   [ATMEGA16U2 Assistant](http://playground.arduino.cc/Bootloader/DueBootloaderExplained),
   the scons command
   
       scons platform=radds upload port=/dev/<usb-device>
        
   may be used to automatically upload the firmware.  You do not need to
   press any buttons on the board to effect the upload.
   
   For boards which lack a Native Programming Port or the ATMEGA16U2
   Assistant, you can use the above command but first you will need to
   press the board's ERASE button.  Possibly the RESET button as well.
   (Note: if you target a Due's Native USB port, you will need to edit
   `src/SConscript` and have the Python code specify `-U true` for the
   bossac command; it presently uses `-U false` for RADDS.)
   
   Boards with an attached Arduino Due should have a Native Programming
   Port as well as the ATMEGA16U2 Assistant (e.g., RADDS).
