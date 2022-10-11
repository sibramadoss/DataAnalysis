module sword_fsm (
    input logic clk, reset, sw,
    output logic v
);
    //wire s10;
    //assign s10 = (reset)
    //dff(clk, s10, s0)

    wire s12;
    assign s12 = ((sw | s12) & ~reset) | (s12 & ~reset & ~sw);
    dff(clk, s12, v);

endmodule


module sword_fsm (
    input logic clk, reset, sw,
    output logic v
);
    wire s10, s11;
    assign s10 = (reset) | (~reset & ~sw & s11);
    dff(clk, s10, s11);

    wire s12;
    assign s12 = (sw & s11 & ~reset) | (~reset & v) | (v & ~reset & ~sw);
    dff(clk, s12, v);

endmodule

