from amaranth import *
from src.rom import *

###########################################
# rv32ui SLTI instruction tests:          #
###########################################

# Simulated ROM image:
slti_rom = rom_img( [
  0x6F004004, 0x732F2034, 0x930F8000, 0x6308FF03, 
  0x930F9000, 0x6304FF03, 0x930FB000, 0x6300FF03, 
  0x130F0000, 0x63040F00, 0x67000F00, 0x732F2034, 
  0x63540F00, 0x6F004000, 0x93E19153, 0x23203050, 
  0x6FF0DFFF, 0x732540F1, 0x63100500, 0x97020000, 
  0x93820201, 0x73905230, 0x73500018, 0x97020000, 
  0x9382C201, 0x73905230, 0x9302F0FF, 0x7390023B, 
  0x9302F001, 0x7390023A, 0x97020000, 0x93828201, 
  0x73905230, 0x73502030, 0x73503030, 0x73504030, 
  0x93010000, 0x97020000, 0x938202F7, 0x73905230, 
  0x13051000, 0x1315F501, 0x634A0500, 0x0F00F00F, 
  0x9308D005, 0x13050000, 0x6F000033, 0x93020000, 
  0x638E0200, 0x73905210, 0xB7B20000, 0x93829210, 
  0x73902230, 0x73232030, 0xE39062F6, 0x73500030, 
  0x37250000, 0x13050580, 0x73200530, 0x97020000, 
  0x93824201, 0x73901234, 0x732540F1, 0x73002030, 
  0x930F0000, 0x631AF02F, 0x97020020, 0x938282FF, 
  0x930FF0FF, 0x13A00F00, 0x23A00200, 0x13030000, 
  0x631C602C, 0x130F1000, 0x93201F80, 0x23A21200, 
  0x13030000, 0x6392602C, 0x930E0000, 0x13A1FEFF, 
  0x23A42200, 0x13030000, 0x6318612A, 0x130EF07F, 
  0x93210E80, 0x23A63200, 0x13030000, 0x639E6128, 
  0x930D0000, 0x13A20D80, 0x23A84200, 0x13030000, 
  0x63146228, 0x97000020, 0x938000FA, 0x371D0000, 
  0x130D0D80, 0x93220D80, 0x23A05000, 0x13010000, 
  0x63942226, 0xB74C6507, 0x938C1C32, 0x13A30C80, 
  0x23A26000, 0x13010000, 0x63182324, 0x370C0080, 
  0x130CFCFF, 0x93231C00, 0x23A47000, 0x13010000, 
  0x639C2322, 0x930B1000, 0x13A40B80, 0x23A68000, 
  0x13010000, 0x63122422, 0x130BF0FF, 0x93240B80, 
  0x23A89000, 0x13010000, 0x63982420, 0x97000020, 
  0x9380C0F3, 0xB71A0000, 0x938A4A23, 0x13A50A80, 
  0x23A0A000, 0x93030000, 0x6318751E, 0x370A0080, 
  0x93250A00, 0x23A2B000, 0x93031000, 0x639E751C, 
  0xB7F9FFFF, 0x9389C9DC, 0x13A6F97F, 0x23A4C000, 
  0x93031000, 0x6312761C, 0x1309F0FF, 0x9326F9FF, 
  0x23A6D000, 0x93030000, 0x6398761A, 0x93081080, 
  0x13A71800, 0x23A8E000, 0x93031000, 0x631E7718, 
  0x17010020, 0x1301C1ED, 0x13080000, 0x93270800, 
  0x2320F100, 0x93010000, 0x63903718, 0x9307F0FF, 
  0x13A80700, 0x23220101, 0x93011000, 0x63163816, 
  0x13071000, 0x93281780, 0x23241101, 0x93010000, 
  0x639C3814, 0x93060000, 0x13A9F6FF, 0x23262101, 
  0x93010000, 0x63123914, 0x1306F07F, 0x93290680, 
  0x23283101, 0x93010000, 0x63983912, 0x97000020, 
  0x938040E8, 0x93050000, 0x13AA0580, 0x23A04001, 
  0x13010000, 0x631A2A10, 0x37150000, 0x13050580, 
  0x932A0580, 0x23A25001, 0x13010000, 0x639E2A0E, 
  0xB7446507, 0x93841432, 0x13AB0480, 0x23A46001, 
  0x13010000, 0x63122B0E, 0x37040080, 0x1304F4FF, 
  0x932B1400, 0x23A67001, 0x13010000, 0x63962B0C, 
  0x93031000, 0x13AC0380, 0x23A88001, 0x13010000, 
  0x631C2C0A, 0x97000020, 0x938000E2, 0x1303F0FF, 
  0x932C0380, 0x23A09001, 0x93030000, 0x639E7C08, 
  0xB7120000, 0x93824223, 0x13AD0280, 0x23A2A001, 
  0x93030000, 0x63127D08, 0x37020080, 0x932D0200, 
  0x23A4B001, 0x93031000, 0x63987D06, 0xB7F1FFFF, 
  0x9381C1DC, 0x13AEF17F, 0x23A6C001, 0x93031000, 
  0x631C7E04, 0x1301F0FF, 0x932EF1FF, 0x23A8D001, 
  0x93030000, 0x63927E04, 0x17010020, 0x130101DC, 
  0x93001080, 0x13AF1000, 0x2320E101, 0x93011000, 
  0x63143F02, 0x13000000, 0x932F0000, 0x2322F101, 
  0x93010000, 0x639A3F00, 0x0F00F00F, 0x9308D005, 
  0x13050000, 0x6FF05FFF, 0x0F00F00F, 0x9308D005, 
  0x37150000, 0x1305D5BA, 0x6FF01FFF, 0x731000C0, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000
] )

# Simulated initialized RAM image:
slti_ram = ram_img( [
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 
  0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 
  0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 
  0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 
  0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 
  0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 
  0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 
  0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 
  0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x80000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000
] )

# Expected 'pass' register values.
slti_exp = {
  768: [ { 'r': 17, 'e': 93 }, { 'r': 10, 'e': 0 } ],  'end': 768
}

# Collected test program definition:
slti_test = [ 'SLTI compliance tests', 'cpu_slti', slti_rom, slti_ram, slti_exp ]