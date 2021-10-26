#include <iostream>
using namespace std;

class Marker{
  private:
    double position;

  public:
    Marker(double iposition){
      position = iposition;
    };

    bool check_rob1_win(){
      return (position > 0.5);
    };
    bool check_rob2_win(){
      return (position < -0.5);
    };
    void rob1_pull(){
      position += ((double) rand() / (RAND_MAX));
    };
    void rob2_pull(){
      position -= ((double) rand() / (RAND_MAX));
    };

};

bool run_trial(double position){
  Marker pointer(position);
  while(pointer.check_rob1_win() != true && pointer.check_rob2_win() != true){
    pointer.rob1_pull();
    if (pointer.check_rob1_win()){
      return true;
    };
    pointer.rob2_pull();
    if (pointer.check_rob2_win()){
      return false;
    };
  };
  return 0;
};

double find_prob(long long num_trials, double position){
  long long num_1wins = 0;
  double result;
  for (int i; i < num_trials; i++){
    if(run_trial(position)){
      num_1wins += 1;
    };
  };
  result = ((double) num_1wins/num_trials);
  cout << result;
  return 0;
};


int main() {
 find_prob(100,0);
}
