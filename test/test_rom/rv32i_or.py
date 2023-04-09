from amaranth import *
from src.rom import *

###########################################
# rv32ui OR instruction tests:            #
###########################################

# Simulated ROM image:
or_rom = rom_img( [
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
  0x9308D005, 0x13050000, 0x6F008040, 0x93020000, 
  0x638E0200, 0x73905210, 0xB7B20000, 0x93829210, 
  0x73902230, 0x73232030, 0xE39062F6, 0x73500030, 
  0x37250000, 0x13050580, 0x73200530, 0x97020000, 
  0x93824201, 0x73901234, 0x732540F1, 0x73002030, 
  0x930F0000, 0x6316F03D, 0x97020020, 0x938282FF, 
  0x930FF0FF, 0x13080000, 0x33E00F01, 0x23A00200, 
  0x13030000, 0x6316603A, 0x130F1000, 0x93071080, 
  0xB360FF00, 0x23A21200, 0x13031080, 0x639A6038, 
  0x930E0000, 0x1307F0FF, 0x33E1EE00, 0x23A42200, 
  0x1303F0FF, 0x631E6136, 0x130EF07F, 0xB7F6FFFF, 
  0x9386C6DC, 0xB361DE00, 0x23A63200, 0x37F3FFFF, 
  0x1303F3FF, 0x639E6134, 0x930D0000, 0x37060080, 
  0x33E2CD00, 0x23A84200, 0x37030080, 0x63126234, 
  0x97000020, 0x938040F8, 0x371D0000, 0x130D0D80, 
  0xB7150000, 0x93854523, 0xB362BD00, 0x23A05000, 
  0x37210000, 0x130141A3, 0x639C2230, 0xB74C6507, 
  0x938C1C32, 0x1305F0FF, 0x33E3AC00, 0x23A26000, 
  0x1301F0FF, 0x631E232E, 0x370C0080, 0x130CFCFF, 
  0x93041000, 0xB3639C00, 0x23A47000, 0x37010080, 
  0x1301F1FF, 0x639E232C, 0x930B1000, 0x37040080, 
  0x1304F4FF, 0x33E48B00, 0x23A68000, 0x37010080, 
  0x1301F1FF, 0x631E242A, 0x130BF0FF, 0xB7436507, 
  0x93831332, 0xB3647B00, 0x23A89000, 0x1301F0FF, 
  0x6390242A, 0x97000020, 0x938040EF, 0xB71A0000, 
  0x938A4A23, 0x37130000, 0x13030380, 0x33E56A00, 
  0x23A0A000, 0xB7230000, 0x938343A3, 0x631A7526, 
  0x370A0080, 0x93020000, 0xB3655A00, 0x23A2B000, 
  0xB7030080, 0x639E7524, 0xB7F9FFFF, 0x9389C9DC, 
  0x1302F07F, 0x33E64900, 0x23A4C000, 0xB7F3FFFF, 
  0x9383F3FF, 0x631E7622, 0x1309F0FF, 0x9301F0FF, 
  0xB3663900, 0x23A6D000, 0x9303F0FF, 0x63927622, 
  0x93081080, 0x13011000, 0x33E72800, 0x23A8E000, 
  0x93031080, 0x63167720, 0x17010020, 0x130141E7, 
  0x13080000, 0x93000000, 0xB3671800, 0x2320F100, 
  0x93010000, 0x6396371E, 0x9307F0FF, 0x13000000, 
  0x33E80700, 0x23220101, 0x9301F0FF, 0x631A381C, 
  0x13071000, 0x930F1080, 0xB368F701, 0x23241101, 
  0x93011080, 0x639E381A, 0x93060000, 0x130FF0FF, 
  0x33E9E601, 0x23262101, 0x9301F0FF, 0x6312391A, 
  0x1306F07F, 0xB7FEFFFF, 0x938ECEDC, 0xB369D601, 
  0x23283101, 0xB7F1FFFF, 0x9381F1FF, 0x63923918, 
  0x97000020, 0x938000E0, 0x93050000, 0x370E0080, 
  0x33EAC501, 0x23A04001, 0x37010080, 0x63122A16, 
  0x37150000, 0x13050580, 0xB71D0000, 0x938D4D23, 
  0xB36AB501, 0x23A25001, 0x37210000, 0x130141A3, 
  0x63902A14, 0xB7446507, 0x93841432, 0x130DF0FF, 
  0x33EBA401, 0x23A46001, 0x1301F0FF, 0x63122B12, 
  0x37040080, 0x1304F4FF, 0x930C1000, 0xB36B9401, 
  0x23A67001, 0x37010080, 0x1301F1FF, 0x63922B10, 
  0x93031000, 0x370C0080, 0x130CFCFF, 0x33EC8301, 
  0x23A88001, 0x37010080, 0x1301F1FF, 0x63122C0E, 
  0x97000020, 0x938040D7, 0x1303F0FF, 0xB74B6507, 
  0x938B1B32, 0xB36C7301, 0x23A09001, 0x9303F0FF, 
  0x63907C0C, 0xB7120000, 0x93824223, 0x371B0000, 
  0x130B0B80, 0x33ED6201, 0x23A2A001, 0xB7230000, 
  0x938343A3, 0x631E7D08, 0x37020080, 0x930A0000, 
  0xB36D5201, 0x23A4B001, 0xB7030080, 0x63927D08, 
  0xB7F1FFFF, 0x9381C1DC, 0x130AF07F, 0x33EE4101, 
  0x23A6C001, 0xB7F3FFFF, 0x9383F3FF, 0x63127E06, 
  0x1301F0FF, 0x9309F0FF, 0xB36E3101, 0x23A8D001, 
  0x9303F0FF, 0x63967E04, 0x17010020, 0x130101CF, 
  0x93001080, 0x13091000, 0x33EF2001, 0x2320E101, 
  0x93011080, 0x63163F02, 0x13000000, 0x93080000, 
  0xB36F1001, 0x2322F101, 0x93010000, 0x639A3F00, 
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
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000
] )

# Simulated initialized RAM image:
or_ram = ram_img( [
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
or_exp = {
  768: [ { 'r': 17, 'e': 93 }, { 'r': 10, 'e': 0 } ],  'end': 768
}

# Collected test program definition:
or_test = [ 'OR compliance tests', 'cpu_or', or_rom, or_ram, or_exp ]