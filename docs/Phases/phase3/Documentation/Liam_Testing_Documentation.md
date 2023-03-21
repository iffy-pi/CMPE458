# Liam Testing Documentation

All code used for testing can be found in /ptsrc/test/phase-3/liam/

## `Module` Testing

The code for testing the module can be found in the file `module_test.pt` The file tests to see if the module declarations emit the correct values and store the module identifier on the stack so it can't be used once again. 

Running the code outputted the following:


## `Public` Procedure Testing

Public procedures were a new form of procedure added to the new Quby language. Similarly to regular procedures, they emit the same T-tokens, however when placed on the symbol stack, the new `syPublicProcedure` symbol is used instead of the normally used `syProcedure` symbol. By delcaring it as a `syPublicProcedure` we can make it accessable outside of the scope of a module. 

Running the `public_procedure_test.pt` file has a module with a public function declared within it. Running semtrace on it returned the following:





## `Multi-Variable` Declaration Testing

Multi-Variable Decleration testing used the `multi_var_declaration_test.pt` and `multi_var_decleration.pt` files and was compiled using the ptsrc-ref compiler and the quby compiler being tested. The file `multi_var_declaration_test.pt` was ran using the quby compiler and is expected to output the same T-tokens as the `multi_var_decleration.pt` file should, when compiled using PT-pascal. 