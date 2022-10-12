module sword_fsm (
    input logic clk, reset, sw,
    output logic v
);
    wire s12;
    assign s12 = ((sw | v) & ~reset) | (v & ~reset & ~sw);
    dff(clk, s12, v);

endmodule


module sword_fsm (
    input logic clk, reset, sw,
    output logic v
);
    wire s10, s11;
    assign s10 = (reset) | (~reset & ~sw & s10);
    dff(clk, s10, s11);

    wire s12;
    assign s12 = (sw & s11 & ~reset) | (~reset & s12) | (s12 & ~reset & ~sw);
    dff(clk, s12, v);

endmodule

