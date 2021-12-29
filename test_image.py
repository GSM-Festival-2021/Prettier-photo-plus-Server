function solution(x1, y1, x2, y2) {
  const x1 = 8;
  const y1 = 4;
  const x2 = 8;
  const y2 = 10;
    let soundSum = 0;

    // 두 스피커 사이가 가까워 음량이 5를 넘는 경우
    if (Math.abs(x1 - x2) + Math.abs(y1 - y2) < 4) return -1;
    if (3 < x1 && x1 < 13 && 3 < x2 && x2 < 13 && 3 < y1 && y1 < 13 && 3 < y2 && y2 < 13) {

        // 벽에 닿지 않는다면 한 스피커당 80 음량을 차지한다.
        soundSum += checkWall(x1, y1)
        soundSum += checkWall(x2, y2)
        soundSum += 160;
        return soundSum;
    } else {function solution() {
  const x1 = 8;
  const y1 = 4;
  const x2 = 8;
  const y2 = 10;

  let room = Array.from(Array(15), () => new Array(15).fill(0));
  let roomSize = 15;
  let xLocation = 0;
  let yLocation = 0;
  let soundSum = 0;

  soundCounting(x1, x2);
  console.log(room);

  if (Math.abs(x1 - x2) + Math.abs(y1 - y2) < 4) return -1;
  if (3 < x1 < 13 && 3 < x2 < 13 && 3 < y1 < 13 && 3 < y2 < 13) {
    soundCounting(x1, x2);
    console.log(room);
  } else {
    return -1;
  }

  function wallSoundCounting() {
    // 아 몰루
  }

  function soundCounting(x, y) {
    // 만약에 벽에 닿는다면

    // 스피커 영역이 겹친다면

    //겹치는 영역이 하나도 없다면
    soundSum += 80;

    for (let i = 0; i < 9; i++) {
      for (let j = 0; j < 9; j++) {
        room[x - 4 + i][y - 4 + j]++;
      }
    }
  }
}

        // 벽에 닿아 음량이 5를 넘는 경우
        return -1;
    }

    function checkWall(x, y) {
        let cnt = 0;
        // 만약에 벽에 소리가 닿는다면
        if (6 > x || x > 10 ) {
            cnt += wallSoundCounting(x);
        }
        if (6 > y || y > 10) {
            cnt += wallSoundCounting(y);
        }

        return cnt;
    }

    function wallSoundCounting(wallLocation) {
        let cnt = 0;
        switch (wallLocation) {
            case 4:
            case 12:
                cnt += 16;
                break;
            case 5:
            case 11:
                cnt += 9;
                break;
        }
        return cnt;
    }
}