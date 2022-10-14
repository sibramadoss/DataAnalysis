module sword_fsm (
    input logic sw, reset, clk
    output logic v
);
    
    wire s00;
    assign s00 = reset | (~reset & ~sw & s0);
    lab04_sr ns (s00, clk, s0);

    wire s01;
    assign s01 = (~reset & sw & s0) | (~reset & s1);
    lab04_sr hs (s01, clk, s1);

    assign v = s1;

endmodule

