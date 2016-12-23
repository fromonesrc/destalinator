#! /usr/bin/env python

import executor


class Archiver(executor.Executor):

    def archive(self):
        print "archive threshold: {}".format(self.config.archive_threshold)
        self.ds.safe_archive_all(self.config.archive_threshold)


if __name__ == "__main__":
    archiver = Archiver()
    archiver.archive()
