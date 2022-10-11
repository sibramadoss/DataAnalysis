module sword_fsm (
    input logic clk, reset, sw,
    output logic v
);

    wire s12;
    assign s12 = (sw | v) & ~reset;
    dff(clk, s12, v);

endmodule




