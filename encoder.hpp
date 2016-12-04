/*
 * =====================================================================================
 *
 *       Filename:  encoder.hpp
 *
 *    Description:  This is the basic header of encoder
 *
 *        Version:  1.0
 *        Created:  11/08/2016 09:03:00 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Pengzhan, Hao 
 *   Organization:  SUNY_Binghamton_CS
 *
 * =====================================================================================
 */

#include <iostream>
#include <stdlib.h>
#include <malloc.h>
#include <math.h>
#include <time.h>

FILE *ifd, *ofd;

int **in_buf, **out_buf;

struct Image_Coord{int x,y;};

static int current_read_byte;
static int current_write_byte;
static int read_position;
static int write_position;

#define MAX(x,y) ((x>y)?x:y)
#define MIN(x,y) ((x>y)?y:x)
#define ABS(x) ((x<0)?-x:x)
