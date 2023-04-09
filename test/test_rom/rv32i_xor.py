from amaranth import *
from src.rom import *

###########################################
# rv32ui XOR instruction tests:           #
###########################################

# Simulated ROM image:
xor_rom = rom_img( [
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
  0x9308D005, 0x13050000, 0x6F008041, 0x93020000, 
  0x638E0200, 0x73905210, 0xB7B20000, 0x93829210, 
  0x73902230, 0x73232030, 0xE39062F6, 0x73500030, 
  0x37250000, 0x13050580, 0x73200530, 0x97020000, 
  0x93824201, 0x73901234, 0x732540F1, 0x73002030, 
  0x930F0000, 0x631EF03D, 0x97020020, 0x938282FF, 
  0x930FF0FF, 0x13080000, 0x33C00F01, 0x23A00200, 
  0x13030000, 0x631E603A, 0x130F1000, 0x93071080, 
  0xB340FF00, 0x23A21200, 0x13030080, 0x6392603A, 
  0x930E0000, 0x1307F0FF, 0x33C1EE00, 0x23A42200, 
  0x1303F0FF, 0x63166138, 0x130EF07F, 0xB7F6FFFF, 
  0x9386C6DC, 0xB341DE00, 0x23A63200, 0x37F3FFFF, 
  0x130333A3, 0x63966136, 0x930D0000, 0x37060080, 
  0x33C2CD00, 0x23A84200, 0x37030080, 0x631A6234, 
  0x97000020, 0x938040F8, 0x371D0000, 0x130D0D80, 
  0xB7150000, 0x93854523, 0xB342BD00, 0x23A05000, 
  0x37210000, 0x130141A3, 0x63942232, 0xB74C6507, 
  0x938C1C32, 0x1305F0FF, 0x33C3AC00, 0x23A26000, 
  0x37C19AF8, 0x1301E1CD, 0x63142330, 0x370C0080, 
  0x130CFCFF, 0x93041000, 0xB3439C00, 0x23A47000, 
  0x37010080, 0x1301E1FF, 0x6394232E, 0x930B1000, 
  0x37040080, 0x1304F4FF, 0x33C48B00, 0x23A68000, 
  0x37010080, 0x1301E1FF, 0x6314242C, 0x130BF0FF, 
  0xB7436507, 0x93831332, 0xB3447B00, 0x23A89000, 
  0x37C19AF8, 0x1301E1CD, 0x6394242A, 0x97000020, 
  0x9380C0EE, 0xB71A0000, 0x938A4A23, 0x37130000, 
  0x13030380, 0x33C56A00, 0x23A0A000, 0xB7230000, 
  0x938343A3, 0x631E7526, 0x370A0080, 0x93020000, 
  0xB3455A00, 0x23A2B000, 0xB7030080, 0x63927526, 
  0xB7F9FFFF, 0x9389C9DC, 0x1302F07F, 0x33C64900, 
  0x23A4C000, 0xB7F3FFFF, 0x938333A3, 0x63127624, 
  0x1309F0FF, 0x9301F0FF, 0xB3463900, 0x23A6D000, 
  0x93030000, 0x63967622, 0x93081080, 0x13011000, 
  0x33C72800, 0x23A8E000, 0x93030080, 0x631A7720, 
  0x17010020, 0x1301C1E6, 0x13080000, 0x93000000, 
  0xB3471800, 0x2320F100, 0x93010000, 0x639A371E, 
  0x9307F0FF, 0x13000000, 0x33C80700, 0x23220101, 
  0x9301F0FF, 0x631E381C, 0x13071000, 0x930F1080, 
  0xB348F701, 0x23241101, 0x93010080, 0x6392381C, 
  0x93060000, 0x130FF0FF, 0x33C9E601, 0x23262101, 
  0x9301F0FF, 0x6316391A, 0x1306F07F, 0xB7FEFFFF, 
  0x938ECEDC, 0xB349D601, 0x23283101, 0xB7F1FFFF, 
  0x938131A3, 0x63963918, 0x97000020, 0x938080DF, 
  0x93050000, 0x370E0080, 0x33CAC501, 0x23A04001, 
  0x37010080, 0x63162A16, 0x37150000, 0x13050580, 
  0xB71D0000, 0x938D4D23, 0xB34AB501, 0x23A25001, 
  0x37210000, 0x130141A3, 0x63942A14, 0xB7446507, 
  0x93841432, 0x130DF0FF, 0x33CBA401, 0x23A46001, 
  0x37C19AF8, 0x1301E1CD, 0x63142B12, 0x37040080, 
  0x1304F4FF, 0x930C1000, 0xB34B9401, 0x23A67001, 
  0x37010080, 0x1301E1FF, 0x63942B10, 0x93031000, 
  0x370C0080, 0x130CFCFF, 0x33CC8301, 0x23A88001, 
  0x37010080, 0x1301E1FF, 0x63142C0E, 0x97000020, 
  0x938080D6, 0x1303F0FF, 0xB74B6507, 0x938B1B32, 
  0xB34C7301, 0x23A09001, 0xB7C39AF8, 0x9383E3CD, 
  0x63907C0C, 0xB7120000, 0x93824223, 0x371B0000, 
  0x130B0B80, 0x33CD6201, 0x23A2A001, 0xB7230000, 
  0x938343A3, 0x631E7D08, 0x37020080, 0x930A0000, 
  0xB34D5201, 0x23A4B001, 0xB7030080, 0x63927D08, 
  0xB7F1FFFF, 0x9381C1DC, 0x130AF07F, 0x33CE4101, 
  0x23A6C001, 0xB7F3FFFF, 0x938333A3, 0x63127E06, 
  0x1301F0FF, 0x9309F0FF, 0xB34E3101, 0x23A8D001, 
  0x93030000, 0x63967E04, 0x17010020, 0x130101CE, 
  0x93001080, 0x13091000, 0x33CF2001, 0x2320E101, 
  0x93010080, 0x63163F02, 0x13000000, 0x93080000, 
  0xB34F1001, 0x2322F101, 0x93010000, 0x639A3F00, 
  0x0F00F00F, 0x9308D005, 0x13050000, 0x6FF05FFF, 
  0x0F00F00F, 0x9308D005, 0x37150000, 0x1305D5BA, 
  0x6FF01FFF, 0x731000C0, 0x00000000, 0x00000000, 
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
xor_ram = ram_img( [
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
xor_exp = {
  768: [ { 'r': 17, 'e': 93 }, { 'r': 10, 'e': 0 } ],  'end': 768
}

# Collected test program definition:
xor_test = [ 'XOR compliance tests', 'cpu_xor', xor_rom, xor_ram, xor_exp ]