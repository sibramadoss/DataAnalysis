module room_fsm (
    input logic clk, n, s, e, w, v, reset,
    output logic s6, win, s5, d, s4, s3, sw, s2, s1, s0
);

    wire s01;
    assign s01 = (s1 & w & ~n & ~s & ~e & ~reset) | (reset) | (~reset & ~n & ~s & ~e & ~w & s0) | (s0 & n & ~reset) | (s0 & s & ~reset) | (s0 & w & ~reset) | (s0 & n & w & ~reset) | (s0 & s & w & ~reset) | (s0 & n & e & ~reset) | (s0 & s & e & ~reset);
    lab04_sr(clk, s01, s0);

    wire s11;
    assign s11 = (s0 & e & ~n & ~w & ~s & ~reset) | (s2 & n & ~e & ~w & ~s & ~reset) | (~reset & ~n & ~s & ~e & ~w & s1) | (s1 & n & ~s & ~e & ~w & ~reset) | (s1 & e & ~n & ~s & ~w & ~reset) | (s1 & n & w & ~e & ~s & ~reset) | (s1 & s & w & ~n & ~e & ~reset) | (s1 & n & e & ~w & ~s & ~reset) | (s1 & s & e & ~n & ~w & ~reset);
    lab04_sr(clk, s11, s1);

    wire s21;
    assign s21 = (s1 & s & ~n & ~w & ~e & ~reset) | (s3 & e & ~n & ~w & ~s  & ~reset) | (~reset & ~n & ~s & ~e & ~w & s2) | (s2 & n & w & ~s & ~e & ~reset) | (s2 & s & w & ~n & ~e & ~reset) | (s2 & n & e & ~w & ~s & ~reset) | (s2 & s & ~w & ~e & ~n & ~reset) | (s2 & ~s & ~w & e & ~n & ~reset);
    lab04_sr(clk, s21, s2);

    wire s31;
    assign s31 = (s2 & w & ~n & ~s & ~e & ~reset) | (~reset & ~n & ~s & ~e & ~w & s3) | (s3 & n & ~e & ~w & ~s & ~reset) | (s3 & s & ~n & ~e & ~w & ~reset) | (s3 & w & ~n & ~e & ~s & ~reset) | (s3 & n & w & ~e & ~s & ~reset) | (s3 & s & w & ~e & ~n & ~reset) | (s3 & n & e & ~s & ~w & ~reset) | (s3 & s & e & ~n & ~w & ~reset);
    assign sw = s3;
    lab04_sr(clk, s31, s3);

    wire s41;
    assign s41 = (s2 & s & e & ~n & ~w & ~reset & (v|~v)) | (~reset & ~n & ~s & ~e & ~w & s4) | (~reset & n & ~s & ~e & ~w & s4) | (~reset & ~n & s & ~e & ~w & s4) | (~reset & ~n & ~s & e & ~w & s4) | (~reset & ~n & ~s & ~e & w & s3) | (~reset & n & ~s & e & ~w & s4) | (~reset & n & ~s & ~e & w & s4) | (~reset & ~n & s & e & ~w & s4) | (~reset & ~n & s & ~e & w & s4);
    lab04_sr(clk, s41, s4);

    wire s51;
    assign s51 = (s4 & v & ~n & ~s & ~w & ~e & ~reset) | (s5 & ~n & ~s & ~w & ~e & ~reset & v) | (s5 & n & ~s & ~w & ~e & ~reset & v) | (s5 & ~n & s & ~w & ~e & ~reset & v) | (s5 & ~n & ~s & w & ~e & ~reset & v) | (s5 & ~n & ~s & ~w & e & ~reset & v) | (s5 & ~n & s & ~w & e & ~reset & v) | (s5 & n & ~s & ~w & e & ~reset & v)  (s5 & ~n & s & w & ~e & ~reset & v) | (s5 & n & ~s & w & ~e & ~reset & v);
    assign win = s5;
    lab04_sr(clk, s51, s5);

    wire s61;
    assign s61 = (s4 & ~v & ~n & ~s & ~w & ~e & ~reset) | (s6 & ~n & ~s & ~w & ~e & ~reset & ~v) | (s6 & n & ~s & ~w & ~e & ~reset & ~v) | (s6 & ~n & s & ~w & ~e & ~reset & ~v) | (s6 & ~n & ~s & w & ~e & ~reset & ~v) | (s6 & ~n & ~s & ~w & e & ~reset & ~v) | (s6 & n & ~s & w & ~e & ~reset & ~v) | (s6 & n & ~s & ~w & e & ~reset & ~v) | (s6 & ~n & s & w & ~e & ~reset & ~v) | (s6 & ~n & s & ~w & e & ~reset & ~v);
    assign d = s6;
    lab04_sr(clk, s61, s6);

endmodule
