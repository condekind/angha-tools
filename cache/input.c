int main(int argc, char *argv[])
{
  int a = argc * 2;
  char b[] = "teste";
  for (int i = 0; i < argc; i++)
    a += argc;
  return a;
}
