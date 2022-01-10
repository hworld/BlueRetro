/*
 * Copyright (c) 2021, Jacques Gagnon
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef _WIRED_COMM_H_
#define _WIRED_COMM_H_

#ifdef CONFIG_BLUERETRO_SYSTEM_PARALLEL_1P
#define HARDCODED_SYS PARALLEL_1P
#else
#ifdef CONFIG_BLUERETRO_SYSTEM_PARALLEL_2P
#define HARDCODED_SYS PARALLEL_2P
#else
#ifdef CONFIG_BLUERETRO_SYSTEM_NES
#define HARDCODED_SYS NES
#else
#ifdef CONFIG_BLUERETRO_SYSTEM_PCE
#define HARDCODED_SYS PCE
#else
#ifdef CONFIG_BLUERETRO_SYSTEM_GENESIS
#define HARDCODED_SYS GENESIS
#else
#ifdef CONFIG_BLUERETRO_SYSTEM_SNES
#define HARDCODED_SYS SNES
#else
#ifdef CONFIG_BLUERETRO_SYSTEM_CDI
#define HARDCODED_SYS CDI
#else
#ifdef CONFIG_BLUERETRO_SYSTEM_CD32
#define HARDCODED_SYS CD32
#else
#ifdef CONFIG_BLUERETRO_SYSTEM_3DO
#define HARDCODED_SYS REAL_3DO
#else
#ifdef CONFIG_BLUERETRO_SYSTEM_JAGUAR
#define HARDCODED_SYS JAGUAR
#else
#ifdef CONFIG_BLUERETRO_SYSTEM_PSX_PS2
#define HARDCODED_SYS PS2
#else
#ifdef CONFIG_BLUERETRO_SYSTEM_SATURN
#define HARDCODED_SYS SATURN
#else
#ifdef CONFIG_BLUERETRO_SYSTEM_PCFX
#define HARDCODED_SYS PCFX
#else
#ifdef CONFIG_BLUERETRO_SYSTEM_JVS
#define HARDCODED_SYS JVS
#else
#ifdef CONFIG_BLUERETRO_SYSTEM_N64
#define HARDCODED_SYS N64
#else
#ifdef CONFIG_BLUERETRO_SYSTEM_DC
#define HARDCODED_SYS DC
#else
#ifdef CONFIG_BLUERETRO_SYSTEM_GC
#define HARDCODED_SYS GC
#else
#ifdef CONFIG_BLUERETRO_SYSTEM_WII_EXT
#define HARDCODED_SYS WII_EXT
#else
#ifdef CONFIG_BLUERETRO_SYSTEM_VBOY
#define HARDCODED_SYS VBOY
#else
#ifdef CONFIG_BLUERETRO_SYSTEM_EXP_BOARD
#define HARDCODED_SYS EXP_BOARD
#endif
#endif
#endif
#endif
#endif
#endif
#endif
#endif
#endif
#endif
#endif
#endif
#endif
#endif
#endif
#endif
#endif
#endif
#endif
#endif

void wired_comm_init(void);
const char *wired_get_sys_name(void);

#endif /* _WIRED_COMM_H_ */
