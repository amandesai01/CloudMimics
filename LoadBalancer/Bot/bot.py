from pickle import PicklingError, pickle

class Report:
    def __init__(self):
        self.requests_sent = 0;
        self.failed_requests = 0;
        self.mean_time = 0;

    def update(self, new_time, failed=False):
        if self.mean_time == 0:
            self.mean_time = new_time
            if failed:
                self.failed_requests += 1
            self.requests_sent += 1
        else:
            self.mean_time = (new_time + self.mean_time)/2
            self.requests_sent += 1

def log(new_time, failed=False):
    report = None
    try:
        report = pickle.load(open("report.pkl", "rb"))
    except PicklingError:
        report = Report()
    report.update(new_time, failed=failed)
    pickle.dump(report, open("report.pkl", "wb"))