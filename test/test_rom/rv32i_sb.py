from amaranth import *
from src.rom import *

###########################################
# rv32ui SB instruction tests:            #
###########################################

# Simulated ROM image:
sb_rom = rom_img( [
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
  0x9308D005, 0x13050000, 0x6F00803D, 0x93020000, 
  0x638E0200, 0x73905210, 0xB7B20000, 0x93829210, 
  0x73902230, 0x73232030, 0xE39062F6, 0x73500030, 
  0x37250000, 0x13050580, 0x73200530, 0x97020000, 
  0x93824201, 0x73901234, 0x732540F1, 0x73002030, 
  0x930F0000, 0x631EF039, 0x97020020, 0x938282FF, 
  0x23800200, 0x1308F0FF, 0x938F0200, 0x23800F01, 
  0x1303F0FF, 0x631E6836, 0x238F02FE, 0x93071000, 
  0x138F0200, 0x230FFFFE, 0x13031000, 0x63926736, 
  0xA3810200, 0x13070000, 0x938E0200, 0xA381EE00, 
  0x13030000, 0x63166734, 0x238E02FE, 0x9306F07F, 
  0x138E0200, 0x230EDEFE, 0x1303F07F, 0x639A6632, 
  0x23810200, 0x13060000, 0x938D0200, 0x2381CD00, 
  0x13030000, 0x631E6630, 0x97000020, 0x9380C0F8, 
  0x23820000, 0xB7150000, 0x93850580, 0x138D0000, 
  0x2302BD00, 0x37110000, 0x13010180, 0x639A252E, 
  0xA38F00FE, 0x37456507, 0x13051532, 0x938C0000, 
  0xA38FACFE, 0x37416507, 0x13011132, 0x631A252C, 
  0xA3800000, 0xB7040080, 0x9384F4FF, 0x138C0000, 
  0xA3009C00, 0x37010080, 0x1301F1FF, 0x639A242A, 
  0x23800000, 0x13041000, 0x938B0000, 0x23808B00, 
  0x13011000, 0x631E2428, 0x238F00FE, 0x9303F0FF, 
  0x138B0000, 0x230F7BFE, 0x1301F0FF, 0x63922328, 
  0x97000020, 0x938080F0, 0xA3810000, 0x37130000, 
  0x13034323, 0x938A0000, 0xA3816A00, 0xB7130000, 
  0x93834323, 0x631E7324, 0x238E00FE, 0xB7020080, 
  0x138A0000, 0x230E5AFE, 0xB7030080, 0x63927224, 
  0x23810000, 0x37F2FFFF, 0x1302C2DC, 0x93890000, 
  0x23814900, 0xB7F3FFFF, 0x9383C3DC, 0x63127222, 
  0x23820000, 0x9301F0FF, 0x13890000, 0x23023900, 
  0x9303F0FF, 0x63967120, 0xA38F00FE, 0x13011080, 
  0x93880000, 0xA38F28FE, 0x93031080, 0x631A711E, 
  0x17010020, 0x1301C1E8, 0xA3000100, 0x93000000, 
  0x13080100, 0xA3001800, 0x93010000, 0x639A301C, 
  0x23000100, 0x1300F0FF, 0x93070100, 0x23800700, 
  0x93010000, 0x631E301A, 0x230F01FE, 0x930F1000, 
  0x13070100, 0x230FF7FF, 0x93011000, 0x63923F1A, 
  0xA3010100, 0x130F0000, 0x93060100, 0xA381E601, 
  0x93010000, 0x63163F18, 0x230E01FE, 0x930EF07F, 
  0x13060100, 0x230ED6FF, 0x9301F07F, 0x639A3E16, 
  0x97000020, 0x938000E2, 0x23810000, 0x130E0000, 
  0x93850000, 0x2381C501, 0x13010000, 0x631A2E14, 
  0x23820000, 0xB71D0000, 0x938D0D80, 0x13850000, 
  0x2302B501, 0x37110000, 0x13010180, 0x639A2D12, 
  0xA38F00FE, 0x374D6507, 0x130D1D32, 0x93840000, 
  0xA38FA4FF, 0x37416507, 0x13011132, 0x631A2D10, 
  0xA3800000, 0xB70C0080, 0x938CFCFF, 0x13840000, 
  0xA3009401, 0x37010080, 0x1301F1FF, 0x639A2C0E, 
  0x23800000, 0x130C1000, 0x93830000, 0x23808301, 
  0x13011000, 0x631E2C0C, 0x97000020, 0x9380C0D9, 
  0x238F00FE, 0x930BF0FF, 0x13830000, 0x230F73FF, 
  0x9303F0FF, 0x639E7B0A, 0xA3810000, 0x371B0000, 
  0x130B4B23, 0x93820000, 0xA3816201, 0xB7130000, 
  0x93834323, 0x631E7B08, 0x238E00FE, 0xB70A0080, 
  0x13820000, 0x230E52FF, 0xB7030080, 0x63927A08, 
  0x23810000, 0x37FAFFFF, 0x130ACADC, 0x93810000, 
  0x23814101, 0xB7F3FFFF, 0x9383C3DC, 0x63127A06, 
  0x23820000, 0x9309F0FF, 0x13810000, 0x23023101, 
  0x9303F0FF, 0x63967904, 0x17010020, 0x130101D2, 
  0xA30F01FE, 0x13091080, 0x93000100, 0xA38F20FF, 
  0x93011080, 0x63163902, 0xA3000100, 0x93080000, 
  0x93000100, 0xA3801001, 0x93010000, 0x639A3800, 
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
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000, 
  0x00000000, 0x00000000, 0x00000000, 0x00000000
] )

# Simulated initialized RAM image:
sb_ram = ram_img( [
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
sb_exp = {
  768: [ { 'r': 17, 'e': 93 }, { 'r': 10, 'e': 0 } ],  'end': 768
}

# Collected test program definition:
sb_test = [ 'SB compliance tests', 'cpu_sb', sb_rom, sb_ram, sb_exp ]