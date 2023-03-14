''' Common constants for Switch devices. '''
from enum import IntEnum, auto
from bit_helper import bit
from .br import axis


class sw(IntEnum):
    ''' Buttons bitfield definition for default reports. '''
    B = 0
    A = auto()
    Y = auto()
    X = auto()
    L = auto()
    R = auto()
    ZL = auto()
    ZR = auto()
    MINUS = auto()
    PLUS = auto()
    LJ = auto()
    RJ = auto()
    HOME = auto()
    CAPTURE = auto()
    SL = auto()
    SR = auto()


class sw_n(IntEnum):
    ''' Buttons bitfield definition for native reports. '''
    Y = 0
    X = auto()
    B = auto()
    A = auto()
    R_SR = auto()
    R_SL = auto()
    R = auto()
    ZR = auto()
    MINUS = auto()
    PLUS = auto()
    RJ = auto()
    LJ = auto()
    HOME = auto()
    CAPTURE = auto()
    DOWN = 16
    UP = auto()
    RIGHT = auto()
    LEFT = auto()
    L_SR = auto()
    L_SL = auto()
    L = auto()
    ZL = auto()


sw_d_btns_mask = [
    0, 0, 0, 0,
    0, 0, 0, 0,
    0, 0, 0, 0,
    0, 0, 0, 0,
    bit(sw.Y), bit(sw.A), bit(sw.B), bit(sw.X),
    bit(sw.PLUS), bit(sw.MINUS), bit(sw.HOME), bit(sw.CAPTURE),
    bit(sw.ZL), bit(sw.L), 0, bit(sw.LJ),
    bit(sw.ZR) | bit(sw.SR), bit(sw.R), 0, bit(sw.RJ),
]


sw_n_btns_mask = [
    0, 0, 0, 0,
    0, 0, 0, 0,
    bit(sw_n.LEFT), bit(sw_n.RIGHT), bit(sw_n.DOWN), bit(sw_n.UP),
    0, 0, 0, 0,
    bit(sw_n.Y), bit(sw_n.A), bit(sw_n.B), bit(sw_n.X),
    bit(sw_n.PLUS), bit(sw_n.MINUS), bit(sw_n.HOME), bit(sw_n.CAPTURE),
    bit(sw_n.ZL), bit(sw_n.L), bit(sw_n.L_SL) | bit(sw_n.R_SL), bit(sw_n.LJ),
    bit(sw_n.ZR), bit(sw_n.R), bit(sw_n.L_SR) | bit(sw_n.R_SR), bit(sw_n.RJ),
]


sw_n_jc_btns_mask = [
    0, 0, 0, 0,
    0, 0, 0, 0,
    0, 0, 0, 0,
    0, 0, 0, 0,
    bit(sw_n.B) | bit(sw_n.UP), bit(sw_n.X) | bit(sw_n.DOWN), bit(sw_n.A) | bit(sw_n.LEFT), bit(sw_n.Y) | bit(sw_n.RIGHT),
    bit(sw_n.CAPTURE) | bit(sw_n.PLUS), bit(sw_n.MINUS) | bit(sw_n.HOME), 0, 0,
    bit(sw_n.L_SL) | bit(sw_n.R_SL), bit(sw_n.ZL) | bit(sw_n.ZR), 0, bit(sw_n.LJ) | bit(sw_n.RJ),
    bit(sw_n.L_SR) | bit(sw_n.R_SR), bit(sw_n.L) | bit(sw_n.R), 0, 0,
]


sw_n_gen_btns_mask = [
    0, 0, 0, 0,
    0, 0, 0, 0,
    bit(sw_n.LEFT), bit(sw_n.RIGHT), bit(sw_n.DOWN), bit(sw_n.UP),
    0, 0, 0, 0,
    bit(sw_n.A), bit(sw_n.R), bit(sw_n.B), bit(sw_n.Y),
    bit(sw_n.PLUS), bit(sw_n.ZR), bit(sw_n.HOME), bit(sw_n.CAPTURE),
    0, bit(sw_n.X), 0, 0,
    0, bit(sw_n.L), 0, 0,
]


sw_n_n64_btns_mask = [
    0, 0, 0, 0,
    bit(sw_n.X), bit(sw_n.MINUS), bit(sw_n.ZR), bit(sw_n.Y),
    bit(sw_n.LEFT), bit(sw_n.RIGHT), bit(sw_n.DOWN), bit(sw_n.UP),
    0, 0, 0, 0,
    bit(sw_n.B), 0, bit(sw_n.A), 0,
    bit(sw_n.PLUS), 0, bit(sw_n.HOME), bit(sw_n.CAPTURE),
    bit(sw_n.ZL), bit(sw_n.L), 0, 0,
    bit(sw_n.LJ), bit(sw_n.R), 0, 0,
]


sw_n_snes_btns_mask = [
    0, 0, 0, 0,
    0, 0, 0, 0,
    bit(sw_n.LEFT), bit(sw_n.RIGHT), bit(sw_n.DOWN), bit(sw_n.UP),
    0, 0, 0, 0,
    bit(sw_n.Y), bit(sw_n.A), bit(sw_n.B), bit(sw_n.X),
    bit(sw_n.PLUS), bit(sw_n.MINUS), 0, 0,
    bit(sw_n.L), bit(sw_n.ZL), 0, 0,
    bit(sw_n.R), bit(sw_n.ZR), 0, 0,
]


sw_n_nes_btns_mask = [
    0, 0, 0, 0,
    0, 0, 0, 0,
    bit(sw_n.LEFT), bit(sw_n.RIGHT), bit(sw_n.DOWN), bit(sw_n.UP),
    0, 0, 0, 0,
    bit(sw_n.B), 0, bit(sw_n.A), 0,
    bit(sw_n.PLUS), bit(sw_n.MINUS), 0, 0,
    bit(sw_n.L), 0, 0, 0,
    bit(sw_n.R), 0, 0, 0,
]


sw_n_pwa_gc_btns_mask = [
    0, 0, 0, 0,
    0, 0, 0, 0,
    bit(sw_n.LEFT), bit(sw_n.RIGHT), bit(sw_n.DOWN), bit(sw_n.UP),
    0, 0, 0, 0,
    bit(sw_n.B), bit(sw_n.X), bit(sw_n.A), bit(sw_n.Y),
    bit(sw_n.PLUS), bit(sw_n.MINUS), bit(sw_n.HOME), bit(sw_n.CAPTURE),
    bit(sw_n.ZL), bit(sw_n.L), 0, bit(sw_n.LJ),
    bit(sw_n.ZR), bit(sw_n.R), 0, bit(sw_n.RJ),
]


sw_rf_brawler64_btns_mask = [
    0, 0, 0, 0,
    bit(sw.X), bit(sw.LJ), bit(sw.Y), bit(sw.RJ),
    0, 0, 0, 0,
    0, 0, 0, 0,
    bit(sw.A), 0, bit(sw.B), 0,
    bit(sw.PLUS), bit(sw.MINUS), bit(sw.HOME), bit(sw.CAPTURE),
    bit(sw.ZL), bit(sw.L), 0, 0,
    bit(sw.ZR), bit(sw.R), 0, 0,
]


sw_hk_admiral_btns_mask = [
    0, 0, 0, 0,
    bit(sw.MINUS), bit(sw.RJ), bit(sw.CAPTURE), bit(sw.HOME),
    0, 0, 0, 0,
    0, 0, 0, 0,
    bit(sw.B), 0, bit(sw.A), 0,
    bit(sw.PLUS), 0, 0, 0,
    bit(sw.SL), bit(sw.L), 0, 0,
    0, bit(sw.R), 0, 0,
]


sw_n_axes = {
    axis.LX: {'neutral': 0x800, 'abs_max': 0x578, 'deadzone': 0xAE},
    axis.LY: {'neutral': 0x800, 'abs_max': 0x578, 'deadzone': 0xAE},
    axis.RX: {'neutral': 0x800, 'abs_max': 0x578, 'deadzone': 0xAE},
    axis.RY: {'neutral': 0x800, 'abs_max': 0x578, 'deadzone': 0xAE},
}


sw_n_ljc_axes = {
    axis.LX: {'neutral': 0x800, 'abs_max': 0x578, 'deadzone': 0xAE, 'polarity': 1},
    axis.LY: {'neutral': 0x800, 'abs_max': 0x578, 'deadzone': 0xAE},
}


sw_n_rjc_axes = {
    axis.LX: {'neutral': 0x800, 'abs_max': 0x578, 'deadzone': 0xAE},
    axis.LY: {'neutral': 0x800, 'abs_max': 0x578, 'deadzone': 0xAE, 'polarity': 1},
}


sw_n_n64_axes = {
    axis.LX: {'neutral': 0x800, 'abs_max': 0x578, 'deadzone': 0xAE},
    axis.LY: {'neutral': 0x800, 'abs_max': 0x578, 'deadzone': 0xAE},
}


sw_rf_brawler64_axes = {
    axis.LX: {'neutral': 0x8000, 'abs_max': 0x8000, 'deadzone': 0},
    axis.LY: {'neutral': 0x8000, 'abs_max': 0x8000, 'deadzone': 0},
}


sw_hk_admiral_axes = {
    axis.LX: {'neutral': 0x8000, 'abs_max': 0x8000, 'deadzone': 0},
    axis.LY: {'neutral': 0x8000, 'abs_max': 0x8000, 'deadzone': 0},
}
