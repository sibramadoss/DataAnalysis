module MUX_MemtoReg(input logic MemtoReg, input logic[31:0] ALUResult, input logic[31:0] RD, output logic[31:0] MemtoReg_out);

    always@(*)
    begin
        case(MemtoReg)
            1'b0 : MemtoReg_out = ALUResult;
            1'b1 : MemtoReg_out = RD;
        default : MemtoReg_out = 0;
        endcase

    end

endmodule


