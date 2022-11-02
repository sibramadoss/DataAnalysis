module top (input logic clk, rst,
input logic [4:0] A1, A2, A3,
input logic [31:0] WD3,
input logic WE3,
input logic [31:0] SrcA,
input logic [31:0] SrcB,
output logic [2:0] ALUControl
output logic [31:0] ALUResult
output logic [31:0] RD1,
output logic [31:0] RD2,
output logic [31:0] prode
);
    regfile reg1 (clk, rst, A1, A2, A3, WD3, WE3, RD1, RD2, prode);

    alu alu1 (SrcA, SrcB, ALUControl, ALUResult);

endmodule

