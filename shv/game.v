module game (
    input logic clk, n, s, e, w, reset,
    output logic s6, win, s5, d, s4, s3, sw, s2, s1, s0, v
);

    room_fsm room1 (clk, n, s, e, w, v, reset, s6, win, s5, d, s4, s3, sw, s2, s1, s0);

    sword_fsm sword1 (sw, reset, clk, v);
    
endmodule

