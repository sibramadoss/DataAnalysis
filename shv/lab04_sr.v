module lab04_sr (
    input logic clk,
    input logic din,
    output logic q
);

    always_ff @(posedge clk) begin
        q <= din;   //blocking assignment
    end

endmodule

