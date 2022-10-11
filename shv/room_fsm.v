module room_fsm (
    input logic clk, n, s, e, w, v, reset,
    output logic s6, win, s5, d, s4, s3, sw, s2, s1, s0
);

    wire s01;
    assign s01 = (s1 & w & ~reset) | (reset) | (~reset & ~n & ~s & ~e & ~w & s01) | (s01 & n & ~reset) | (s01 & s & ~reset) | (s01 & w & ~reset) | (s01 & n & w & ~reset) | (s01 & s & w & ~reset) | (s01 & n & e & ~reset) | (s01 & s & e & ~reset);
    dff(clk, s01, s0);

    wire s11;
    assign s11 = (s0 & e & ~reset) | (s2 & n & ~reset) | (s11 & ~reset) | (~reset & ~n & ~s & ~e & ~w & s11) | (s11 & n & ~reset) | (s11 & e & ~reset) | (s11 & n & w & ~reset) | (s11 & s & w & ~reset) | (s11 & n & e & ~reset) | (s11 & s & e & ~reset);
    dff(clk, s11, s1);

    wire s21;
    assign s21 = (s1 & s & ~reset) | (s3 & e & ~reset) | (s21 & ~reset) | (~reset & ~n & ~s & ~e & ~w & s21) | (s21 & s & ~reset) | (s21 & e & ~reset) | (s21 & n & w & ~reset) | (s21 & s & w & ~reset) | (s21 & n & e & ~reset);
    dff(clk, s21, s2);

    wire s31;
    assign s31 = (s2 & w & ~reset) | (s31 & ~reset) | (~reset & ~n & ~s & ~e & ~w & s31) | (s31 & n & ~reset) | (s31 & s & ~reset) | (s31 & w & ~reset)  | (s31 & w & ~reset) | (s31 & n & w & ~reset) | (s01 & s & w & ~reset) | (s31 & n & e & ~reset) | (s31 & s & e & ~reset);
    assign sw = s3;
    dff(clk, s31, s3);

    wire s41;
    assign s41 = (s2 & s & e & ~reset) | (s41 & ~reset);
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




