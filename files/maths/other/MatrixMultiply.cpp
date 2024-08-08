matrix MatrixMultiply(const matrix &A, const matrix &B) {
    // If MatrixMultiply is passed without any index vector arguments we
    // want to multiply the full matrices together. This wrapper constucts
    // the necessary vectors for that and passes them to MatrixMultiply.

    indvec R(A.Rows());
    indvec V(A.Cols());  // or equivalently V(B.Rows());
    indvec C(B.Cols());
    return MatrixMultiply(A, B, R, V, C);
}
