/*
 * Copyright (c) 2024 Rebecca G. Bettencourt
 * SPDX-License-Identifier: Apache-2.0
 */

`default_nettype none

module tt_um_rebeccargb_tungsten (
    input  wire [7:0] ui_in,    // Dedicated inputs
    output wire [7:0] uo_out,   // Dedicated outputs
    input  wire [7:0] uio_in,   // IOs: Input path
    output wire [7:0] uio_out,  // IOs: Output path
    output wire [7:0] uio_oe,   // IOs: Enable path (active high: 0=input, 1=output)
    input  wire       ena,      // always 1 when the design is powered, so you can ignore it
    input  wire       clk,      // clock
    input  wire       rst_n     // reset_n - low to reset
);

  assign uo_out[7] = uio_in[{rst_n ? ui_in[0] : clk, ui_in[7:6]}];
  assign uo_out[6] = uio_in[ui_in[7:5]];
  assign uo_out[5] = uio_in[ui_in[6:4]];
  assign uo_out[4] = uio_in[ui_in[5:3]];
  assign uo_out[3] = uio_in[ui_in[4:2]];
  assign uo_out[2] = uio_in[ui_in[3:1]];
  assign uo_out[1] = uio_in[ui_in[2:0]];
  assign uo_out[0] = uio_in[{ui_in[1:0], rst_n ? ui_in[7] : clk}];

  // All output pins must be assigned. If not used, assign to 0.
  assign uio_out = 0;
  assign uio_oe  = 0;

  // List all unused inputs to prevent warnings
  wire _unused = &{ena, clk, rst_n, 1'b0};

endmodule
