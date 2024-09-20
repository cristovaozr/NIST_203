# static const struct {
#   const char *name; // test name
#   const uint8_t ek[PKE512_EK_SIZE]; // test ek (800 bytes)
#   const uint8_t m[32]; // test message (32 bytes)
#   const uint8_t enc_rand[32]; // test randomness (32 bytes)
#   const uint8_t exp[PKE512_CT_SIZE]; // expected ciphertext (768 bytes)
# }

# https://github.com/pablotron/fips203ipd/blob/main/fips203ipd.c#L13566

PKE512_ENCRYPT_TESTS = {
    "name": "rand = 0, message = 1",
    "ek": [
        0x12, 0xba, 0x8d, 0xea, 0x4c, 0x7f, 0xf2, 0xf5, 0x02, 0xdd, 0x67, 0x9c,
        0xc8, 0x01, 0x60, 0xef, 0xdc, 0x76, 0x06, 0xb2, 0x64, 0x2f, 0x85, 0xac,
        0xed, 0xa0, 0xcf, 0xdf, 0xb8, 0x0b, 0x7a, 0x41, 0x6f, 0x55, 0xf2, 0xb1,
        0x96, 0x2b, 0x47, 0x03, 0x1c, 0xca, 0x43, 0xc0, 0x8d, 0x82, 0x40, 0x58,
        0xfb, 0x45, 0x84, 0x34, 0xb1, 0x24, 0x32, 0xd5, 0x97, 0xc5, 0x74, 0x18,
        0x0d, 0x91, 0x0d, 0x8a, 0x25, 0x31, 0xee, 0x0a, 0x43, 0xf4, 0x33, 0x9c,
        0x77, 0x74, 0x0f, 0x36, 0x24, 0xa0, 0x0a, 0x93, 0x6b, 0x64, 0x5b, 0x1d,
        0x54, 0x92, 0x10, 0xd4, 0x53, 0x81, 0x9e, 0x0c, 0x4a, 0xcd, 0x2c, 0x4d,
        0x77, 0x70, 0x14, 0xde, 0x98, 0xcd, 0x98, 0x1a, 0xa0, 0x00, 0x3b, 0x01,
        0x5c, 0x33, 0x98, 0xad, 0x77, 0x60, 0x06, 0x28, 0x4a, 0xba, 0x49, 0x41,
        0x7a, 0x53, 0x51, 0xd0, 0xc5, 0x6a, 0x70, 0x9a, 0x4d, 0x05, 0x5a, 0x77,
        0x47, 0x06, 0x8f, 0xe6, 0x60, 0x45, 0x42, 0xf6, 0x73, 0x22, 0xd8, 0x59,
        0x99, 0x2a, 0x34, 0x71, 0x50, 0xab, 0x9a, 0x39, 0x22, 0x7e, 0x4b, 0xa2,
        0xc9, 0xe8, 0x2e, 0xd8, 0xca, 0x60, 0xad, 0xbb, 0xbb, 0xf5, 0xa9, 0x08,
        0xd3, 0x67, 0xa8, 0x9a, 0x1a, 0x39, 0xd4, 0xf6, 0x2b, 0x21, 0x82, 0x9a,
        0x01, 0xf4, 0x4b, 0x22, 0xa7, 0x56, 0x2c, 0xfc, 0x8d, 0xe2, 0xbc, 0x0a,
        0xeb, 0xa8, 0x5e, 0xcf, 0x90, 0x4f, 0x82, 0x70, 0xa1, 0x08, 0x6a, 0xaa,
        0x25, 0x80, 0x43, 0xa1, 0xb6, 0x89, 0xd3, 0xe9, 0x56, 0x24, 0x95, 0x36,
        0x7e, 0xd0, 0x55, 0xd6, 0x60, 0x7c, 0x48, 0x0c, 0x38, 0x9a, 0x38, 0x04,
        0xa0, 0x01, 0x56, 0xd8, 0x10, 0x50, 0x1d, 0xc5, 0x87, 0x13, 0x4c, 0x1a,
        0xf3, 0x15, 0x75, 0x78, 0xb9, 0x51, 0x39, 0xf6, 0x56, 0xa9, 0x8b, 0x4c,
        0x95, 0x08, 0x08, 0x0f, 0x65, 0x8c, 0xf3, 0x11, 0x44, 0x4d, 0xb9, 0x25,
        0x78, 0x51, 0xbf, 0xee, 0xf1, 0x2c, 0x26, 0xa6, 0x6f, 0x79, 0x19, 0x54,
        0xfd, 0xb5, 0xb7, 0xec, 0x67, 0x55, 0x98, 0x5a, 0xb0, 0x06, 0x22, 0xa7,
        0x8e, 0x7b, 0x6c, 0x9e, 0x9c, 0x94, 0xf6, 0xd8, 0x30, 0xe3, 0x4c, 0x0e,
        0x44, 0x17, 0x8a, 0x29, 0x37, 0x64, 0x65, 0x29, 0xb1, 0x7b, 0x57, 0x74,
        0x71, 0x29, 0x8d, 0x1d, 0x3b, 0x8e, 0x14, 0x60, 0x04, 0xdd, 0xb0, 0x0c,
        0xde, 0xba, 0x34, 0xda, 0x33, 0x15, 0x30, 0xd8, 0x6d, 0xca, 0x71, 0x3c,
        0xb2, 0x73, 0xb7, 0xe0, 0xc4, 0xae, 0x16, 0x26, 0x97, 0x1a, 0xe1, 0x32,
        0xa4, 0xa6, 0x18, 0x12, 0x62, 0x35, 0xd3, 0x33, 0x83, 0xd7, 0xe2, 0x69,
        0xe1, 0xa2, 0x09, 0x99, 0x12, 0xcc, 0xb5, 0xe9, 0x21, 0x80, 0x6b, 0xc3,
        0x26, 0x42, 0x04, 0xb4, 0x94, 0x11, 0x45, 0xec, 0x71, 0x2e, 0xe8, 0x71,
        0x47, 0x58, 0x28, 0xa2, 0x08, 0x31, 0x05, 0x6a, 0x5c, 0x5d, 0x49, 0xba,
        0x77, 0xf3, 0x2b, 0xa1, 0xc3, 0x9c, 0xcd, 0x2c, 0xaa, 0xc8, 0x37, 0x9b,
        0x73, 0x17, 0x5d, 0xae, 0x40, 0x29, 0xe8, 0x30, 0x6b, 0x02, 0x04, 0xc7,
        0x3e, 0xe7, 0xa5, 0x36, 0x16, 0x52, 0x71, 0x22, 0xb3, 0xec, 0xdb, 0x2a,
        0xe0, 0xd8, 0xa7, 0xfe, 0x33, 0x23, 0x07, 0xe1, 0x5a, 0x7c, 0x50, 0xbd,
        0x95, 0x40, 0x31, 0xbf, 0x8b, 0x18, 0x13, 0x46, 0x13, 0x6a, 0xd1, 0xa4,
        0x8b, 0xc7, 0x95, 0xdd, 0x69, 0xc0, 0xab, 0xe4, 0x48, 0x38, 0x43, 0xb2,
        0x00, 0x2d, 0x69, 0x40, 0x75, 0x22, 0x47, 0xa7, 0x6e, 0x69, 0x85, 0x80,
        0x11, 0x57, 0x34, 0x99, 0x07, 0x19, 0xe6, 0x6b, 0x7e, 0x49, 0x8c, 0x5c,
        0xab, 0x76, 0xc5, 0x2d, 0xc5, 0x5f, 0x1b, 0x75, 0xc8, 0xeb, 0x78, 0xc9,
        0x14, 0x39, 0xa6, 0x7c, 0x78, 0x85, 0xd0, 0xea, 0x68, 0xdf, 0x40, 0xc2,
        0xb1, 0x21, 0x39, 0xb9, 0x91, 0x39, 0x2a, 0xe8, 0x04, 0xdb, 0x53, 0x4f,
        0x99, 0x65, 0x4c, 0xa3, 0x7b, 0x60, 0xc2, 0xa8, 0x63, 0x98, 0xeb, 0x4d,
        0x54, 0xfa, 0x98, 0x04, 0xc8, 0xc3, 0x35, 0xa5, 0xcc, 0xde, 0xeb, 0x52,
        0xa8, 0x10, 0x41, 0x27, 0x1b, 0xb0, 0xa8, 0xb4, 0x48, 0xe8, 0xe1, 0x0b,
        0x27, 0xb9, 0x03, 0xd3, 0xc9, 0x98, 0x8e, 0xc9, 0x4b, 0xbf, 0x74, 0xb0,
        0x20, 0xd7, 0x35, 0x32, 0xf6, 0xac, 0x32, 0x49, 0x25, 0xf4, 0x19, 0x40,
        0xc6, 0xf7, 0x23, 0xf9, 0xf8, 0x47, 0x54, 0x73, 0x8d, 0xae, 0x87, 0x40,
        0xc0, 0x92, 0x0f, 0x85, 0xe0, 0xaa, 0x31, 0x69, 0x69, 0x78, 0x18, 0x75,
        0xa6, 0xbc, 0xbe, 0x6c, 0x29, 0xbe, 0x01, 0xda, 0x65, 0x93, 0x12, 0xc0,
        0xf6, 0xd8, 0x88, 0xee, 0xa8, 0xa5, 0x65, 0x31, 0x5d, 0x7f, 0x01, 0x0a,
        0x74, 0xe5, 0x35, 0x07, 0xf4, 0xb3, 0x41, 0xc7, 0x0e, 0x38, 0x33, 0x9b,
        0x30, 0x3b, 0x85, 0x92, 0x5a, 0x08, 0x96, 0x13, 0x9f, 0x7c, 0x29, 0x3b,
        0x07, 0x64, 0x06, 0x59, 0x18, 0x86, 0x75, 0xe1, 0xaf, 0xcd, 0x21, 0x91,
        0x40, 0xf0, 0x59, 0xce, 0x7a, 0x8e, 0xfa, 0x52, 0x77, 0x05, 0xb0, 0xb6,
        0xcf, 0x82, 0x99, 0x8a, 0xda, 0x37, 0x41, 0xdc, 0xb2, 0x97, 0x18, 0xad,
        0x6f, 0x50, 0xba, 0x1d, 0xf3, 0x4c, 0x42, 0x62, 0x5c, 0xd6, 0x91, 0xc4,
        0xe5, 0x45, 0x3b, 0x76, 0x0a, 0xb3, 0xae, 0xb2, 0x16, 0x5c, 0xeb, 0x4e,
        0x2a, 0xf3, 0x5f, 0x77, 0xe0, 0x45, 0xb6, 0xd0, 0x42, 0x5c, 0x91, 0x0d,
        0x7b, 0xc2, 0x76, 0x85, 0xf4, 0x3b, 0x49, 0xc7, 0xbc, 0x6f, 0x53, 0x20,
        0x3d, 0xe1, 0x23, 0xef, 0xc7, 0x20, 0x50, 0xd0, 0x4d, 0x27, 0xcb, 0x33,
        0x68, 0xcc, 0x3d, 0x7a, 0xe4, 0x3d, 0x8d, 0x76, 0x18, 0xeb, 0xa4, 0x19,
        0xad, 0x56, 0xc3, 0x5c, 0xab, 0x50, 0x63, 0xb9, 0xe7, 0xea, 0x56, 0x83,
        0x14, 0xec, 0x81, 0xc4, 0x0b, 0xa5, 0x77, 0xaa, 0xe6, 0x30, 0xde, 0x90,
        0x20, 0x04, 0x00, 0x9e, 0x88, 0xf1, 0x8d, 0xa5,],

    "m": b'\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    "enc_rand": b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',

    "exp": [
        0x62, 0xab, 0xd0, 0xc6, 0x57, 0x54, 0x84, 0x04, 0x9d, 0x39, 0x85, 0xab,
        0xed, 0x84, 0x52, 0x30, 0x7d, 0xf6, 0x2a, 0x1a, 0xa0, 0xe6, 0xc7, 0xd3,
        0x8f, 0x97, 0xff, 0x53, 0x5d, 0xec, 0x9c, 0x18, 0x77, 0x47, 0xf8, 0x1d,
        0x88, 0x51, 0x39, 0xf5, 0xc3, 0x08, 0x7a, 0x08, 0xff, 0xea, 0xf6, 0x49,
        0xc7, 0xaa, 0x28, 0xec, 0xe9, 0x1c, 0x65, 0xd0, 0x4c, 0x15, 0x53, 0x10,
        0x46, 0x82, 0x7c, 0x4e, 0x19, 0xbb, 0xc0, 0xbf, 0xaa, 0x66, 0x53, 0xb7,
        0x64, 0xb6, 0xbe, 0xd6, 0x15, 0x1e, 0x9a, 0x2e, 0x03, 0x4b, 0x02, 0xa7,
        0xa3, 0x7b, 0x2d, 0x36, 0x0b, 0x0d, 0xad, 0x0b, 0x64, 0xec, 0x3c, 0x42,
        0x82, 0xf0, 0xd8, 0x8a, 0x66, 0xf3, 0x16, 0xd7, 0x47, 0xbd, 0x16, 0xa2,
        0x8f, 0xc8, 0x55, 0xc9, 0x3d, 0xfd, 0x84, 0x86, 0x12, 0x53, 0x33, 0x18,
        0x5a, 0x19, 0xa7, 0x85, 0x4b, 0xa6, 0x3d, 0xed, 0xea, 0xac, 0xbc, 0x6c,
        0x5d, 0xf8, 0x9c, 0x19, 0xf0, 0xeb, 0xc1, 0x77, 0x0c, 0x0e, 0xa1, 0xb2,
        0xec, 0x2a, 0x1c, 0xe2, 0x7e, 0xc4, 0x4f, 0xfd, 0x0a, 0xed, 0xaf, 0x8b,
        0xf5, 0x37, 0xb0, 0xfc, 0x51, 0x6b, 0x19, 0xd8, 0x14, 0x60, 0xa5, 0xf9,
        0xed, 0xa3, 0x09, 0x99, 0xe0, 0xb9, 0xdb, 0xef, 0x5d, 0x5f, 0x2e, 0xdb,
        0x40, 0xb2, 0x96, 0xc5, 0xcc, 0x47, 0x2c, 0xb2, 0xba, 0x83, 0x69, 0x1a,
        0xd3, 0x60, 0xad, 0xfb, 0x7a, 0xfa, 0x04, 0x51, 0xaa, 0x23, 0x22, 0x5e,
        0x13, 0xdb, 0x71, 0x88, 0xe7, 0x8b, 0xc0, 0x4f, 0x27, 0x33, 0xd2, 0x74,
        0x15, 0x6a, 0x06, 0x75, 0x17, 0xaf, 0x71, 0x7c, 0x5d, 0x4b, 0xff, 0x0d,
        0x5d, 0x63, 0x52, 0x37, 0xdc, 0xd2, 0x22, 0xef, 0x55, 0x50, 0xe9, 0xb1,
        0xa1, 0x70, 0x41, 0xc0, 0xc1, 0x79, 0xc2, 0x4e, 0x8d, 0xa5, 0x03, 0x0b,
        0x05, 0x72, 0x94, 0x88, 0x26, 0xe4, 0xc4, 0xd1, 0xb4, 0x8f, 0x06, 0x96,
        0xa7, 0xc7, 0x32, 0x4f, 0x33, 0x04, 0x1f, 0x1a, 0xff, 0x84, 0x40, 0x11,
        0x08, 0x95, 0xb8, 0x02, 0x8f, 0x09, 0xae, 0x93, 0xf4, 0x56, 0x1d, 0x82,
        0xde, 0x2f, 0x77, 0xf4, 0x41, 0x54, 0xcd, 0xe6, 0xc3, 0xf2, 0xb7, 0x69,
        0x82, 0xe8, 0x37, 0x24, 0x4f, 0x2e, 0xb0, 0x9f, 0xea, 0x99, 0xd1, 0x9b,
        0x1e, 0x70, 0xa9, 0x26, 0xe4, 0xf5, 0xc6, 0xad, 0x18, 0xac, 0xa7, 0xba,
        0xe6, 0x98, 0x71, 0x58, 0x30, 0x6c, 0xe4, 0x2d, 0xd6, 0x8f, 0x70, 0xd4,
        0xb0, 0xca, 0xdb, 0x7b, 0x37, 0xad, 0x0b, 0x5c, 0xe6, 0x40, 0xec, 0x02,
        0x24, 0x04, 0xec, 0xff, 0x38, 0xb9, 0xfe, 0xa7, 0x9a, 0x3e, 0x02, 0x5c,
        0x25, 0x6b, 0x3f, 0xd2, 0x8c, 0x85, 0x41, 0x09, 0x28, 0xc0, 0x06, 0xc2,
        0xb3, 0x93, 0x7d, 0xfa, 0x9f, 0x2c, 0x40, 0x43, 0xa9, 0x2f, 0x9c, 0x25,
        0x96, 0x15, 0x7b, 0x33, 0x7e, 0xe9, 0xa9, 0xe9, 0x57, 0xe7, 0x05, 0xf7,
        0xa4, 0x1b, 0x25, 0x07, 0xc8, 0x8d, 0x6e, 0xa1, 0xc7, 0x79, 0x33, 0x9f,
        0x25, 0x64, 0xe1, 0x9c, 0x88, 0x92, 0x2a, 0xa4, 0xb6, 0x7a, 0x2b, 0x25,
        0xf3, 0x5b, 0x0f, 0xa3, 0xd1, 0x0c, 0x91, 0xb5, 0xcd, 0x59, 0x73, 0xd8,
        0xfe, 0x73, 0x3f, 0xf0, 0x21, 0x56, 0x54, 0x2d, 0x25, 0x44, 0x9b, 0x1f,
        0x15, 0x7a, 0xbf, 0x1b, 0x68, 0xc0, 0x4f, 0xa0, 0xf9, 0xe8, 0xc0, 0x6f,
        0x86, 0xa5, 0x26, 0x17, 0x5a, 0x20, 0x61, 0x9e, 0x26, 0x6e, 0xd4, 0xca,
        0xc1, 0xfb, 0xeb, 0x90, 0x40, 0x27, 0x73, 0xb3, 0x3b, 0x09, 0xf5, 0xa9,
        0xc8, 0xe8, 0xb7, 0xc6, 0x1e, 0x8d, 0xe4, 0x68, 0x60, 0x5b, 0x47, 0x8e,
        0x05, 0x39, 0x9d, 0x77, 0x0d, 0xfe, 0x6e, 0xe7, 0x90, 0xd6, 0x12, 0xf8,
        0x2a, 0xcc, 0x03, 0xf2, 0x94, 0x11, 0xdb, 0x4c, 0x75, 0x77, 0x1d, 0xbc,
        0x0d, 0x0d, 0x63, 0x20, 0xe0, 0xdc, 0xed, 0x64, 0x8f, 0x96, 0x71, 0x90,
        0xe5, 0xdb, 0xd3, 0xde, 0x6d, 0x27, 0x45, 0x62, 0x30, 0xaa, 0x3d, 0xcf,
        0x9f, 0xa0, 0x53, 0xdc, 0x9d, 0xb8, 0x7f, 0xd3, 0xad, 0xe8, 0x1b, 0x25,
        0x21, 0x0e, 0x5c, 0xfc, 0x4f, 0x7c, 0x89, 0x9d, 0x00, 0x27, 0x78, 0xb5,
        0xdf, 0xff, 0xde, 0x75, 0x2e, 0x08, 0x55, 0x7d, 0x48, 0x4c, 0x05, 0x8c,
        0x4d, 0x82, 0xa8, 0xfd, 0x2b, 0x90, 0x35, 0x56, 0x5d, 0xc7, 0xdd, 0xa0,
        0xa5, 0x50, 0x7d, 0xc4, 0x15, 0x7d, 0x12, 0x18, 0xa4, 0x8d, 0xca, 0x26,
        0xe5, 0x5c, 0xf2, 0x3d, 0x05, 0xd2, 0x27, 0xe9, 0x11, 0x96, 0xee, 0x40,
        0x18, 0x43, 0xfd, 0x11, 0xa1, 0xde, 0x03, 0x83, 0xae, 0xd7, 0xb3, 0xdc,
        0xf4, 0x04, 0x70, 0x65, 0xe0, 0x3e, 0xb9, 0xbf, 0x5f, 0x16, 0x71, 0xfb,
        0x87, 0x34, 0xf0, 0xc4, 0xfb, 0x30, 0x3c, 0x58, 0xe6, 0x55, 0xb6, 0x90,
        0xb0, 0x72, 0xed, 0xfe, 0xfa, 0x8d, 0xac, 0xc4, 0x4c, 0x78, 0x5c, 0xd4,
        0x71, 0x34, 0x68, 0xf9, 0x5f, 0x4a, 0xd5, 0x83, 0xc7, 0x9c, 0x19, 0x7c,
        0x16, 0x87, 0x62, 0x8c, 0x7c, 0x79, 0xcd, 0x4e, 0xe2, 0x3a, 0x55, 0x5e,
        0xca, 0x3e, 0x46, 0xb4, 0x8f, 0x4e, 0x31, 0x21, 0xd1, 0x98, 0xcc, 0x9d,
        0xdc, 0x00, 0xa5, 0x60, 0xdc, 0x3e, 0x96, 0x69, 0xc7, 0x3f, 0x05, 0xfd,
        0x36, 0x6e, 0x49, 0x9f, 0xa2, 0xc9, 0x74, 0x1f, 0x79, 0xe0, 0x25, 0x44,
        0x76, 0xa9, 0x9c, 0xaa, 0xb9, 0xe1, 0x42, 0x9c, 0x84, 0x15, 0x8f, 0x57,
        0x86, 0xe3, 0x4c, 0x13, 0xa6, 0xc1, 0xcc, 0x33, 0x72, 0x28, 0x84, 0x95,
        0xef, 0xcf, 0xa8, 0xa5, 0x41, 0xf6, 0xad, 0x86, 0x01, 0xd7, 0xd8, 0xa8,
        0xb4, 0x5c, 0xd8, 0x5e, 0x81, 0x71, 0xd3, 0x87, 0x6a, 0xea, 0x11, 0xe6,
    ]
}

# ek = bytes(PKE512_ENCRYPT_TESTS['ek'])
# m = PKE512_ENCRYPT_TESTS['m']
# enc_rand = PKE512_ENCRYPT_TESTS['enc_rand']
# exp = bytes(PKE512_ENCRYPT_TESTS['exp'])
#
# c = my_kpke.Encrypt(ek, m, enc_rand)
#
# print(c == exp)