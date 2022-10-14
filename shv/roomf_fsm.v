module room_fsm (
    input logic clk, n, s, e, w, v, reset,
    output logic s6, win, s5, d, s4, s3, sw, s2, s1, s0
);

wire s00, s01, s02, s03, s04, s05, s06;

assign s00 = reset | ~reset & ((s1 & w & ~(n|s|e)) | (s0 & n & ~(s|e|w)) | (s0 & s & ~(n|e|w)) | (s0 & w & ~(s|e|n)) | (s0 & (n&e) & ~(s|w)) | (s0 & (s&e) & ~(n|w)) | (s0 & (n&w) $ ~(s|e)) | (s0 & (s&w) $ ~(n|e))) | (s0 & ~(n|s|e|w) & ~reset) ;
lab04_sr cc (clk, s00, s0);

assign s01 = ~reset & ((s0 & e & ~(n|s|w)) | (s2 & n & ~(e|s|w)) | (s1 & e & ~(n|s|w)) | (s1 & n & ~(e|s|w)) | (s1 & (s&e) & ~(w|n)) | (s1 & (n&e) & ~(s|w)) | (s1 & (n&w) & ~(e|s)) | (s1 & (s&w) & ~(e|n)) | (s1 & ~(n|e|s|w)));
lab04_sr tt (clk, s01, s1); 

assign s02 = ~reset & ((s1 & s & ~(n|e|w)) | (s3 & e & ~(s|n|w)) | (s2 & e & ~(n|s|w)) | (s2 & (n&e) & ~(s|w)) | (s2 & (n&w) & ~(e|s)) | (s2 & (s&w) & ~(n|e)) | (s2 & s & ~(n|e|w)) | (s2 & ~(n|s|e|w)));
lab04_sr rr (clk, s02, s2);

assign s03 = ~reset & ((s2 & w & ~(n|e|s)) | (s3 & n & ~(e|s|w)) | (s3 & s & ~(e|n|w)) | (s3 & w & ~(e|s|n)) | (s3 & (n&w) & ~(e|s)) | (s3 & (s&w) & ~(n|e)) | (s3 & (n&e) & ~(s|w)) | (s3 & (s&e) & ~(n|w)) | (s3 & ~(n|s|e|w)));
lab04_sr ss (clk, s03, s3);
assign sw = s3;

assign s04 = (~reset & s2 & s & e);
lab04_sr dd (clk, s04, s4);

assign s05 = (~reset & s4 & ~v) | (s5 & ~reset);
lab04_sr gg (clk, s05, s5);
assign d = s5;

assign s06 = (~reset & s4 & v) | (s6 & ~reset);
lab04_sr vv (clk, s06, s6);
assign win = s6;

endmodule


