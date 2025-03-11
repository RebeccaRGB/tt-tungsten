# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    # Set the clock period to 10 us (100 KHz)
    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())

    # Reset
    dut._log.info("Reset")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1

    dut._log.info("Test project behavior")

    # Set the input values you want to test
    dut.ui_in.value = 23
    dut.uio_in.value = 192

    # Wait for one clock cycle to see the output values
    await ClockCycles(dut.clk, 1)

    # The following assersion is just an example of how to check the output values.
    # Change it to match the actual expected output of your module:
    assert dut.uo_out.value == 3

    # Keep testing the module by changing the input values, waiting for
    # one or more clock cycles, and asserting the expected output values.

    dut.uio_in.value = 0
    for x in range(256):
        dut.ui_in.value = x
        await ClockCycles(dut.clk, 1)
        assert dut.uo_out.value == 0

    dut.uio_in.value = 255
    for x in range(256):
        dut.ui_in.value = x
        await ClockCycles(dut.clk, 1)
        assert dut.uo_out.value == 255

    dut.uio_in.value = 204
    for x in range(256):
        dut.ui_in.value = x
        await ClockCycles(dut.clk, 1)
        assert dut.uo_out.value == x

    dut.uio_in.value = 51
    for x in range(256):
        dut.ui_in.value = x
        await ClockCycles(dut.clk, 1)
        assert dut.uo_out.value == 255 - x

    dut.uio_in.value = 170
    for x in range(256):
        dut.ui_in.value = x
        await ClockCycles(dut.clk, 1)
        assert dut.uo_out.value == ((x << 1) | (x >> 7)) & 255

    dut.uio_in.value = 85
    for x in range(256):
        dut.ui_in.value = x
        await ClockCycles(dut.clk, 1)
        assert dut.uo_out.value == 255 - (((x << 1) | (x >> 7)) & 255)

    dut.uio_in.value = 240
    for x in range(256):
        dut.ui_in.value = x
        await ClockCycles(dut.clk, 1)
        assert dut.uo_out.value == ((x << 7) | (x >> 1)) & 255

    dut.uio_in.value = 15
    for x in range(256):
        dut.ui_in.value = x
        await ClockCycles(dut.clk, 1)
        assert dut.uo_out.value == 255 - (((x << 7) | (x >> 1)) & 255)

    testCases = [
        #RULE PREV NEXT
        (192,  23,   3),
        (160,  23,  10),
        (136,  23,   6),
        (252,  23, 159),
        (250,  23, 175),
        (238,  23,  63),
        ( 60,  23, 156),
        ( 90,  23, 165),
        (102,  23,  57),
    ]
    for r, p, n in testCases:
        dut.ui_in.value = p
        dut.uio_in.value = r
        await ClockCycles(dut.clk, 1)
        assert dut.uo_out.value == n
        dut.uio_in.value = 255 - r
        await ClockCycles(dut.clk, 1)
        assert dut.uo_out.value == 255 - n
