module MUX_ALUSrc(input logic ALUSrc, input logic[31:0] RD2, input logic[31:0] SignImm, output logic[31:0] SrcB);

    always@(*)
    begin
        case(ALUSrc)
            1'b0 : SrcB = RD2;
            1'b1 : SrcB = SignImm;
        default : SrcB = 0;
        endcase

    end

endmodule
