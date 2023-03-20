module MUX_RegDst(input logic RegDst, input logic[4:0] rs, input logic[4:0] rd, output logic[4:0] WriteReg);

    always@(*)
    begin
        case(RegDst)
            1'b0 : WriteReg = rs;
            1'b1 : WriteReg = rd;
        default : WriteReg = 0;
        endcase

    end

endmodule

