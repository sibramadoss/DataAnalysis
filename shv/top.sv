module top(
input logic clk, rst,
input logic[1:0] sw, //address for instruction memory
output logic[31:0] ALUResult, //output for pre-lab simulation
output logic[31:0] RD1, RD2, //output for pre-lab simulation
output logic[31:0] prode_register_file, //output for pre-lab simulation
output logic[6:0] display_led, //output for in-lab
output logic[31:0] MemtoReg_out,
output logic[31:0]SignImm,
output logic[31:0] RD,
output logic[31:0] SrcB,
output logic[4:0] WriteReg
);


logic[31:0] inst_0 = 32'b0;
logic[31:0] inst_1 = 32'b010101_00000_00001_0000_0000_0000_0101; 
//add rf_regs[5] and rf_regs[4] to rf_regs[1];
logic[31:0] inst_2 = 32'b010100_00000_00110_0000_0000_0000_0010; 
//sub rf_regs[10] - rf_regs[8] to rf_regs[1];
logic[31:0] inst_ex;
assign inst_ex = (sw==1)? inst_1:(sw==2)? inst_2: inst_0;
register_file r_f(.clk(clk),.rst(rst),
.A1(inst_ex[25:21]),.A2(inst_ex[20:16]),.A3(WriteReg[4:0]),
.WD3(ALUResult),
.WE3(1),
.RD1(RD1),
.RD2(RD2),
//.prode(prode_register_file)
);
ALU t1(
.SrcA(RD1),
.SrcB(RD2),
.ALUControl(inst_ex[29:27]),
.ALUResult(ALUResult)
);
data_memory d1(.clk(clk),.rst(rst),
.A(ALUResult),
.WD(RD2),
.WE(0),
.RD(RD),
.prode(prode_register_file)
);
MUX_MemtoReg(
.ALUResult(ALUResult),
.RD(RD),
.MemtoReg(inst_ex[26]),
.MemtoReg_out(MemtoReg_out)
);
MUX_ALUSrc(
.RD2(RD2),
.SignImm(SignImm),
.ALUSrc(inst_ex[30]),
.SrcB(SrcB)
);
MUX_RegDst(
.rs(inst_ex[25:21]),
.rd(inst_ex[15:11]),
.RegDst(inst_ex[31]),
.WriteReg(WriteReg)
);
sign_extend(
.SignImm(SignImm),
.Imm(inst_ex[15:0])
);
display t2(.data_in(prode_register_file), 
.segments(display_led)); 
endmodule
