module room_fsm (
    input logic clk, n, s, e, w, v, reset,
    output logic s6, win, s5, d, s4, s3, sw, s2, s1, s0
);

    wire s01;
    assign s01 = (s1 & w & ~reset) | (reset);
    dff(clk, s01, s0);

    wire s11;
    assign s11 = (s0 & e & ~reset) | (s2 & n & ~reset) | (s11 & ~reset);
    dff(clk, s11, s1);

    wire s21;
    assign s21 = (s1 & s & ~reset) | (s3 & e & ~reset) | (s21 & ~reset);
    dff(clk, s21, s2);

    wire s31;
    assign s31 = (s2 & w & ~reset) | (s31 & ~reset);
    assign sw = s3;
    dff(clk, s31, s3);

    wire s41;
    assign s41 = (s2 & (s & e) & ~reset) | (s41 & ~reset);
    dff(clk, s41, s4);

    wire s51;
    assign s51 = (s4 & v & ~reset) | (s51 & ~reset);
    assign win = s5;
    dff(clk, s51, s5);

    wire s61;
    assign s61 = (s4 & ~v & ~reset) | (s61 & ~reset);
    assign d = s6;
    dff(clk, s61, s6);

endmodule



